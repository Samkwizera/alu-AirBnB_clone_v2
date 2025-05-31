#!/usr/bin/python3

from fabric.api import *
import os

env.hosts = ['142.44.167.228', '144.217.246.195']


def do_clean(number=0):
    if number == 0:
        number = 1
    number = int(number)
    if number < 0:
        return False
    with lcd("versions"):
        local("ls -t | tail -n +{} | xargs -I {{}} rm -- {{}}".format(number + 1))
    with cd("/data/web_static/releases"):
        run("ls -t | tail -n +{} | xargs -I {{}} rm -rf -- {{}}".format(number + 1)) 