#!/usr/bin/env python

import argh


ALL_PACKAGES_URL = "https://bower-component-list.herokuapp.com/"
BASE_PACKAGE_URL = "https://bower.herokuapp.com/packages"


def package_to_uri(package):
    return package


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


def install():
    pass


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
