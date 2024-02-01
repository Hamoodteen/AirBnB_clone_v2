#!/usr/bin/python3
""" commentttttttttttttttttttttttt """
from fabric import task, Connection
from datetime import datetime


def do_pack(do):
    """ commentttttttttttttttttttttttt """
    do.local(f"mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file = f"web_static_{time}.tgz"
    dir = f"versions/{file}"
    correct = do.local(f"tar -czf {dir} -C web_static .")
    return dir if not correct.failed else None
