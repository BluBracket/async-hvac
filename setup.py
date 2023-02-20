#!/usr/bin/env python
import os
import sys
from importlib import util
from setuptools import setup, find_packages
from pkg_resources import resource_filename

spec = util.spec_from_file_location(
    "async_hvac.version", os.path.join("async_hvac", "version.py")
)
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)  # type: ignore
version = mod.version  # type: ignore

setup(
    name='async-hvac',
    version=version,
    description='HashiCorp Vault API client',
    long_description='HashiCorp Vault API python 3.6+ client using asyncio (forked from https://github.com/Aloomaio/async-hvac).',  # noqa: E501
    author='BluBracket',
    author_email='info@blubracket.com',
    url='https://github.com/blubracket/async-hvac',
    keywords=['hashicorp', 'vault', 'hvac'],
    classifiers=['License :: OSI Approved :: Apache Software License'],
    packages=find_packages(),
    install_requires=[
        'aiohttp==3.8.4',
        'importlib-metadata>=0.12',
    ],
    include_package_data=True,
    extras_require={
        'parser': ['pyhcl==0.3.10']
    }
)
