#! /usr/bin/env python
# coding: utf-8

import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "portfolio")
)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "libs"))


if __name__ == '__main__':
    from portfolio.application import app

    app.debug = True
    app.run(host='0.0.0.0')
