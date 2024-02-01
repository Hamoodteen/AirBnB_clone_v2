#!/usr/bin/python3
""" commentttttttttttttttttttttttt """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ commentttttttttttttttttttttttt """
    local(f"mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file = f"web_static_{time}.tgz"
    dir = f"versions/{file}"
    correct = local(f"tar -czf {dir} -C web_static .")
    return dir if not correct.failed else None
