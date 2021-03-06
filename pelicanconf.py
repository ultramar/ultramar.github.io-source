#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Henrique'
SITENAME = u'Ultramar'
#SITESUBTITLE = u'Polemos Pyrinos'
#SITEURL = 'http://ultramar.github.io'
SITEURL = 'http://localhost:8000'
TYPOGRIFY = True

TIMEZONE = 'Europe/London'

DATE_FORMATS = {
    'pt': ('pt_PT','%d de %B de %Y'),
}

THEME = 'themes/pelican-pageturner'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

DEFAULT_PAGINATION = 5

MENUITEMS = [
    ('Rol','/'),
    ('Arquivo','/archives.html'),
]

MD_EXTENSIONS = ['extra', 'footnotes', 'toc']

PLUGIN_PATH = "plugins"
PLUGINS = ['optimize_images', 'summary', 'post_stats', 'interlinks']

DISQUS_SITENAME = 'ultramar-io'
DISQUS_DEVMODE = True

GOOGLE_ANALYTICS = "UA-45193555-1"

STATIC_PATHS = ['images']