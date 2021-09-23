# -*- coding: utf-8 -*-
"""
Project: Tutorials
File Name: setup
Author: wjz
date: 2021-09-13
"""
from distutils.core import setup
from Cython.Build import cythonize

setup(name="hello app",
      ext_modules=cythonize("hello.pyx"))