# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in ciss_management/__init__.py
from ciss_management import __version__ as version

setup(
	name='ciss_management',
	version=version,
	description='The App will manage CISS Projects',
	author='Internet Stewards',
	author_email='mike@musya.me.ke',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
