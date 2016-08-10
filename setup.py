#!/usr/bin/env python

import os
import sys

from pip.req import parse_requirements
from setuptools import setup, find_packages

needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
sphinx = ['sphinx'] if needs_sphinx else []
needs_wheel = {'bdist_wheel'}.intersection(sys.argv)
wheel = ['wheel'] if needs_wheel else []

setup_dir = os.path.dirname(os.path.realpath(__file__))
path_req = os.path.join(setup_dir, 'requirements.txt')
install_reqs = parse_requirements(path_req, session=False)

reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='pgoapi',
    version='1.1.6',
    description='Pokemon Go API lib',
    author='tjado',
    url='https://github.com/tejado/pgoapi',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Games/Entertainment',
        'Topic :: Games/Entertainment :: Role-Playing',
        'Topic :: Software Development :: Libraries',
    ],
    license='MIT',
    install_requires=reqs,
    setup_requires=sphinx + wheel,
)
