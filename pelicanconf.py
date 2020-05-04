#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Popcorn'
SITENAME = 'Hotpotpy_Blog'
SITEURL = ''


PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = "../Flex"
SITELOGO = "/images/profile2.png"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/aaron-fung-4aa518a1'),
          ('github', 'https://github.com/hotpotpy'),
          )

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = []
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True