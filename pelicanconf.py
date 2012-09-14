#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Dominique Lederer"
SITENAME = u"return1"
SITESUBTITLE = u'"return true" quality webapplications'
SITEURL = 'http://return1.at'
#TWITTER_USERNAME = 'return1_at'

TIMEZONE = 'Europe/Vienna'

DEFAULT_LANG = 'en'

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/return1_at'),
          ('google+', 'https://plus.google.com/113955961996209596236/about'),
          ('github', 'https://github.com/return1'),
          ('linkedin', 'http://at.linkedin.com/in/dominiquelederer'),
          ('xing', 'https://www.xing.com/profile/Dominique_Lederer'),
          ('about.me', 'https://about.me/dominique.lederer/'),
    )

DEFAULT_PAGINATION = 5

THEME = "themes/return1"

STATIC_PATHS = ['images','assets','sandbox']

LOCALE = 'en_US.UTF-8'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

SUMMARY_MAX_LENGTH = 30

# A list of files to copy from the source to the destination
FILES_TO_COPY = (
    ('assets/robots.txt', 'robots.txt'),
    ('assets/favicon.ico', 'favicon.ico'),
    )

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'

#seo
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
