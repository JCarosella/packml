#!/usr/bin/env python3

from setuptools import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['packml_gui'],
    package_dir={'': 'src'},
    scripts=['scripts/packml']
)

setup(**d)
