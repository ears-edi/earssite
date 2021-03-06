#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'ears-edi'
SITENAME = 'Edinburgh University EaRS'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'ears-edi.github.io'

# the below is a path as well as the name of the theme
THEME = 'pelican-blue'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

GOOGLE_ANALYTICS = 'UA-92880122-1'

FAVICON = '/images/favicon.ico'

# Theme specific options
# Enables sidebar to have listing of pages
DISPLAY_PAGES_ON_MENU = True
# Adds summary to events on main page
DISPLAY_SUMMARY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"
ARTICLE_URL = "events/{slug}"
ARTICLE_SAVE_AS = "events/{slug}.html"

# Social widget
SOCIAL = (('Facebook', 'https://fb.me/earsedi'),
          ('GitHub', 'https://github.com/ears-edi'),
          ('LinkedIn','https://www.linkedin.com/company/ears-edi/'),
          ('Instagram','https://www.instagram.com/earsedinburgh/'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
