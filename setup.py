#!/usr/bin/env python

from distutils.core import setup

setup(name='cosm',
      version='1.0',
      description='Python Cosm Daemon',
      author='Keith Baker',
      author_email='kbaker@alumni.ithaca.edu',
      url='https://github.com/krbaker/cosmd',
      packages=['cosm'],
      scripts=['cosmd'],
      data_files=[('/etc/', ['cosm.conf'])],
     )
