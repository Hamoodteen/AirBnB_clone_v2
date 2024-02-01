#!/usr/bin/python3
""" commentttttttttttttttttttttttt """
from fabric.api import *
import os


def do_deploy(archive_path):
    """ commentttttttttttttttttttttttt """
    if not os.path.exists(archive_path):
        return False
    return True
