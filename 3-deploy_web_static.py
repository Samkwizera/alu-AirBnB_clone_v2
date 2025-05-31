#!/usr/bin/python3

from fabric.api import env
from datetime import datetime
from os.path import exists
from do_pack import do_pack
from do_deploy_web_static import do_deploy

env.hosts = ['142.44.167.228', '144.217.246.195']


def deploy():
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path) 