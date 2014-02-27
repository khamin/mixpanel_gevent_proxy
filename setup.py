#!/usr/bin/env python
# -*- coding: utf-8 -

from setuptools import setup, find_packages


PACKAGES = find_packages()


setup(
	name = 'mixpanel_gevent_proxy',
	version = '1.0',
	packages = PACKAGES,
	package_dir = {'': '.'},
	author = 'Vitaliy Khamin',
	author_email = 'vitaliykhamin@gmail.com',
	maintainer = 'Vitaliy Khamin',
	maintainer_email = 'vitaliykhamin@gmail.com',
	description = 'Mixpanel Gevent Proxy',
	url = '',
	zip_safe = True,

	platforms = (
		'any',
	),

	classifiers = (
		'Operating System :: OS Independent',
		'Programming Language :: Python',
	),

	dependency_links = [
	],

	install_requires = [
		'gevent',
		'mixpanel-py',
	],

	entry_points = {
		'console_scripts': [
			'mixpanel_gevent_proxy = mixpanel_gevent_proxy:main',
		],
	},
)
