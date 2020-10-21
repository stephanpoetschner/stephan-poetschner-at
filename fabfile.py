# coding: utf-8
import sys, os

from fabric.api import *
from fabric import colors
from fabric.contrib.console import confirm
from fabric.contrib.project import rsync_project
from fabric.contrib.console import confirm


env.hosts = [ "poetschner", ]
env.root = "/home/stephan/apps/stephan_poetschner_at/"
env.PROJECT_ROOT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    ""
)
env.OUTPUT_DIR = os.path.join(env.PROJECT_ROOT, 'build', '')

def deploy():
    puts(u"Syncing project folders")
    rsync_project(env.root, env.OUTPUT_DIR)

