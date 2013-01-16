# coding: utf-8
import os
from flask import Flask, render_template, make_response, url_for, redirect

from md_content.core import ContentFolder

app = Flask(__name__)

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

app.config.update(
    FREEZER_DEFAULT_MIMETYPE='text/html',
    FREEZER_DESTINATION='../build',
    FREEZER_BASE_URL='http://stephan-poetschner.at/',
    FREEZER_IGNORE_MIMETYPE_WARNINGS=True,

    CONTENT_FOLDER=os.path.join(PROJECT_ROOT, 'content'),
)

app.config.from_object('portfolio.default_settings')
app.reader = ContentFolder(app.config['CONTENT_FOLDER'])

def annotate_items(d):
    return dict( (k, v % d) for (k, v) in d.items() )


@app.route('/')
def index():
    site_vars = app.config['SITE']
    context = annotate_items(site_vars)

    context['projects'] = app.reader.projects.sort(key=lambda x: x['date'], reverse=True)
    context['events'] = app.reader.events.sort(key=lambda x: x['date'], reverse=True)
    context['skills'] = app.reader.skills.sort(key=lambda x: x['order'])

    return render_template('index.html', **context)
