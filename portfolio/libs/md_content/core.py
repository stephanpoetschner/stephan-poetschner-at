# coding: utf-8
import os
import yaml

from dateutil import parser as date_parser
from markdown import Markdown

class MetadataError(Exception):
    pass

class MarkdownError(Exception):
    pass

class ContentFile(object):
    file_extensions = [ 'md', 'markdown', 'mkd', 'mdown', ]
    _md = Markdown()

    def __init__(self, path):

        if not ContentFile.is_valid(path):
            raise RuntimeError("'%s' is not a valid ContentFile." % path)

        dirname, filename = os.path.split(path)

        self._path = path
        self.name = filename

        self.meta = dict()
        self.content = ""

        self.read()

    def __repr__(self):
        name, _ = os.path.splitext(os.path.basename(self._path))
        return "<%s (%s)>" % ( self.__class__.__name__, name, )

    def __str__(self):
        return self.content

    def __getitem__(self, key):
        return self.meta.get(key)

    @classmethod
    def is_valid(cls, path):
        if not os.path.isfile(path):
            return False

        name, ext = os.path.splitext(path)
        if ext.lstrip('.') not in cls.file_extensions:
            return False

        return True

    def split(self, data):
        is_meta = True
        metadata_lines = []
        md_lines = []

        for line in data.splitlines():
            if not is_meta:
                md_lines.append(line)
            else:
                metadata_lines.append(line)

            if line.startswith('---'):
                is_meta = False

        return '\n'.join(metadata_lines[:-1]), '\n'.join(md_lines)


    def annotate_meta(self, meta):
        if 'date' in meta:
            meta['date'] = date_parser.parse(str(meta['date']))
        return meta

    def parse(self, contents):
        raw_metadata, md = self.split(contents)

        try:
            self.meta = dict(yaml.safe_load(raw_metadata))
        except yaml.scanner.ScannerError:
            raise MetadataError(self._path)

        self.meta = self.annotate_meta(self.meta)

        self.content = self._md.reset().convert(md)

        return self.meta, self.content


    def read(self):
        with open(self._path, encoding='utf-8') as f:
            metadata, content = self.parse(f.read().strip())
            return metadata, content



class ContentIterator(object):
    def __init__(self, items, key=None, reverse=False):
        self.items = sorted(items, key=key, reverse=reverse)
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.items):
            raise StopIteration

        item = self.items[self.i]
        self.i += 1

        return item

    def sorted(self, sort_key):
        return ContentIterator(self.items, key=sort_key)



class ContentFolder(object):

    def __init__(self, path):
        path = os.path.abspath(path)

        self._path = path
        self._files = []
        self._folders = []

        for filename in os.listdir(self._path):
            abspath = os.path.join(self._path, filename)
            if os.path.isfile(abspath) and ContentFile.is_valid(abspath):
                self._add_file(abspath)
            elif os.path.isdir(abspath):
                self._add_folder(abspath)

    def __repr__(self):
        return os.path.basename(self._path)


    def _add_file(self, filepath):
        if not ContentFile.is_valid(filepath):
            return

        dirname, filename = os.path.split(filepath)
        name, ext = os.path.splitext(filename)


        try:
            d = ContentFile(filepath)
        except (MetadataError, MarkdownError):
            return

        setattr(
            self,
            name,
            d
        )
        self._files.append(d)

    def _add_folder(self, dirpath):
        _, basename = os.path.split(dirpath)

        d = ContentFolder(dirpath)
        setattr(
            self,
            basename,
            d
        )
        self._folders.append(d)

    @property
    def folders(self):
        for folder in self._folders:
            yield folder

    @property
    def files(self):
        return self.__iter__()

    def __iter__(self):
        return ContentIterator(self._files)

    def sort(self, key=None, reverse=False):
        return ContentIterator(self._files, key=key, reverse=reverse)
