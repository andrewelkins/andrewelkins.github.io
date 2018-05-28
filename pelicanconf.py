#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

AUTHOR = 'Andrew Elkins'
SITENAME = 'Andrew Elkins'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = '/home/andrew/Sites/andrew/andrewelkins.github.io/themes/MinimalXY'

# Theme customizations
MINIMALXY_FAVICON = 'favicon.ico'
MINIMALXY_START_YEAR = 2008
MINIMALXY_CURRENT_YEAR = datetime.datetime.now().year
DISPLAY_CATEGORIES_ON_MENU = 0

# Author
AUTHOR_INTRO = u'Andrew Elkins'
AUTHOR_DESCRIPTION = u'Exploring data engineering'
AUTHOR_AVATAR = 'https://www.gravatar.com/avatar/9ce362310261da087478fb439d9002c2?s=240'
AUTHOR_WEB = 'https://andrewelkins.com'

# Services
GOOGLE_ANALYTICS = 'UA-9318136-7'

# Social
SOCIAL = (
        ('twitter', 'http://twitter.com/andrewelkins'),
        ('github', 'https://github.com/andrewelkins'),
        ('linkedin', 'http://www.linkedin.com/in/andrewelkins'),

)

# Menu
MENUITEMS = (
        ('Categories', '/categories.html'),
        ('Archive', '/archives.html'),

)
