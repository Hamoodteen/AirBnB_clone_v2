#!/usr/bin/python3
""" commentttttttttttttttttttttttt """
from fabric import Connection
from fabric.api import *
import os


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
