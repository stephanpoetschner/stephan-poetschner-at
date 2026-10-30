# Flask-based Portfolio generator

* see my [portfolio](http://stephan-poetschner.at) for a live demo.
* see http://flask.readthedocs.org for Flask-related documentation.
* see https://pythonhosted.org/Frozen-Flask/ for Frozen-Flask-related documentation.

Requires [uv](https://docs.astral.sh/uv/); it installs Python and dependencies on first run.

## Regenerate site

    ./freeze.py     # writes ./build/
    ./deploy.sh     # freeze + rsync to server

## Run debug server

    ./runserver.py

Visit http://localhost:8000/


## Add content

create files in `./content` folder
