#!/usr/bin/python3
""" commentttttttttttttttttttttttt """
from fabric import task, Connection


def do_pack(do):
    """ commentttttttttttttttttttttttt """
    dir = "/web_static"
    file = "/versions/web_static_<year><month><day><hour><minute><second>.tgz"
    correct = do.local(f"tar -czf {file} -C {dir} .")
    return file if not correct.failed else None
