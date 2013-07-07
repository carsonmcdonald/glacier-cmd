#!/usr/bin/env python
import os
from setuptools import setup, find_packages

from glaciercmd import __version__

setup(
    name='glaciercmd',
    version=__version__,
    author='Carson McDonald',
    author_email='carson@ioncannon.net',
    description='Command line interface for AWS Glacier',
    license='MIT',
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    url="http://github.com/carsonmcdonald/glacier-cmd",
    packages=find_packages(),
    install_requires=['boto'],
    data_files=[],
    entry_points={
        'console_scripts': ['glaciercmd = glaciercmd.cli:run',]
    },
)
