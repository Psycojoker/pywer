#!/usr/bin/env python

import re
import json
import argh

from os import path
from urllib2 import urlopen


ALL_PACKAGES_URL = "https://bower-component-list.herokuapp.com/"
BASE_PACKAGE_URL = "https://bower.herokuapp.com/packages"


class GithubRepos(object):
    def __init__(self, uri):
        self.uri = uri
        self.author = uri[len("git://github.com/"):].split("/")[0]
        self.name = uri[len("git://github.com/"):].split("/")[1].split(".")[0]


def package_to_uri(package):
    if package.startswith(("https://", "http://", "git://")):
        return package

    if "/" in package:
        if package.endswith(".git"):
            return "git://github.com/" + package
        else:
            return "git://github.com/" + package + ".git"

    if re.match("^[a-z0-9.-]+$", package):
        return json.load(urlopen(path.join(BASE_PACKAGE_URL, package)))["url"]

    raise Exception("Unhandle package query:" % package)


# commands
def cache():
    pass


def help():
    pass


def home():
    pass


def info():
    pass


def init():
    pass


def install(*packages):
    print dict(zip(packages, map(GithubRepos, map(package_to_uri, packages))))


def link():
    pass


def list():
    pass


def lookup():
    pass


def prune():
    pass


def register():
    pass


def search():
    pass


def update():
    pass


def uninstall():
    pass


parser = argh.ArghParser()
parser.add_commands([cache, help, home, info, init, install, link, list, lookup, prune, register, search, update, uninstall])

if __name__ == '__main__':
    parser.dispatch()
