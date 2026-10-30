#!/bin/sh
# Build the static site and sync it to the web server.
set -eu
cd "$(dirname "$0")"
./freeze.py
rsync -av build/ poetschner:/home/stephan/apps/stephan_poetschner_at/
