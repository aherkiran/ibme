# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in ibme/__init__.py
from ibme import __version__ as version

setup(
	name='ibme',
	version=version,
	description='Language Expert',
	author='IBME',
	author_email='aherkiran765@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
