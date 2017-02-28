#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'ears-edi'
SITENAME = 'Edinburgh University EaRS'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'ears-edi.github.io'

THEME = 'pelican-blue'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"
ARTICLE_URL = "blog/{slug}"
ARTICLE_SAVE_AS = "blog/{slug}.html"

# Social widget
SOCIAL = (('Facebook', 'https://fb.me/earsedi'),
          ('GitHub', 'https://github.com/ears-edi'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
