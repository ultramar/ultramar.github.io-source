#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://ultramar.github.io'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL

FEED_ALL_ATOM = 'feed/all.atom.xml'
CATEGORY_FEED_ATOM = 'feed/%s.atom.xml'

FEED_ALL_RSS = 'feed/all.rss.xml'
CATEGORY_FEED_RSS = 'feed/%s.rss.xml'

DELETE_OUTPUT_DIRECTORY = True

DISQUS_DEVMODE = False
THEME = 'themes/pelican-pageturner'

