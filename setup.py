import os
import sys

from setuptools import setup, find_packages

ROOT = os.path.realpath(os.path.join(os.path.dirname(
    sys.modules['__main__'].__file__)))

# Add Sentry to path so we can import distutils
sys.path.insert(0, os.path.join(ROOT, 'portfolio'))

VERSION = '0.1.dev0'

install_requires=[
    'Flask',
    'Frozen-Flask',
    'Markdown',
    'PyYAML',
    'python-dateutil',

    'markdown_storage',
]

setup(
    name='stephan-poetschner-at-portfolio',
    version=VERSION,

    package_dir={'': 'portfolio'},
    packages=find_packages('portfolio'),
    include_package_data=True,

    install_requires=install_requires,
)