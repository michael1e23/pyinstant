#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.rst') as file:
    long_description = file.read()

setup(
    name = "pyinstant",
    version = "0.1",
    author = "Michael Isik",
    author_email = "isikmichael@gmx.net",

    description = "Instantly start python script by skipping initialization procedures.",
    license = "GPLv3",
    url = "https://github.com/michael1e23/pyinstant",
    download_url = "https://github.com/michael1e23/pyinstant/tarball/master",

    #packages = find_packages(),
    py_modules = ['pyinstant'],

    long_description = long_description,
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX",
        "Programming Language :: Python",
    ],

    platforms = ["Linux"],
)
