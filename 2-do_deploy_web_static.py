#!/usr/bin/python3
""" commentttttttttttttttttttttttt """
from fabric.api import local, put, run
import os


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
