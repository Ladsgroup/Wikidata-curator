# -*- coding: utf-8  -*-
"""Installer script for Wikidata Curator."""
#
# (C) Amir Sarabadani
#
# Distributed under the terms of the MIT license.
#
import os

from setuptools import find_packages, setup


def requirements(fname):
    return [line.strip()
            for line in open(os.path.join(os.path.dirname(__file__), fname))]


setup(
    name='wd_curator',
    version='0.0.1',
    description='A tool to curate new items in Wikidata.',
    long_description=open('README.md').read(),
    maintainer='Amir Sarabadani',
    maintainer_email='ladsgroup@gmail.com',
    license='MIT License',
    install_requires=requirements("requirements.txt"),
    packages=find_packages(),
    url='https://github.com/Ladsgroup/Wikidata-curator',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ],
)
