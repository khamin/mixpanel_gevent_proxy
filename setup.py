#!/usr/bin/env python
# -*- coding: utf-8 -

from setuptools import setup


setup(
	name = 'mixpanel_gevent_proxy',
	version = '1.0',

	packages = [
		'mixpanel_gevent_proxy'
	],

	package_dir = {'': '.'},

	author = 'Vitaliy Khamin',
	author_email = 'vitaliykhamin@gmail.com',
	maintainer = 'Vitaliy Khamin',
	maintainer_email = 'vitaliykhamin@gmail.com',
	description = 'Mixpanel Gevent Proxy',
	url = 'https://github.com/khamin/mixpanel_gevent_proxy',
	zip_safe = True,

	classifiers = (
		'Operating System :: OS Independent',
		'Programming Language :: Python'
	),

	dependency_links = [
	],

	install_requires = [
		'gevent',
		'mixpanel-py'
	],

	entry_points = {
		'console_scripts': [
			'mixpanel_gevent_proxy = mixpanel_gevent_proxy:main'
		]
	}
)
