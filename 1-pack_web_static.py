#!/usr/bin/python3

from fabric.api import local
from time import strftime
from datetime import date

def do_pack():
    '''A script which generates a .tgz archive from the contents of the webstatic folderof airbnb clone repo'''
    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/".format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None

