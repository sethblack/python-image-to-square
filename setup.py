#!/usr/bin/env python3

from os import path
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='image2square',
    version='1.0.0',
    description='Takes an image and force it into a square with gaussian blurred background as filler.',
    author='Seth Black',
    author_email='sblack@sethserver.com',
    url='https://github.com/sethblack/python-image-to-square',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    entry_points={
        'console_scripts' : [
            'image2square = image2square.__main__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU GPL",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
