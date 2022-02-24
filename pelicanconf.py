#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Dominique Lederer"
SITENAME = u"return1"
SITESUBTITLE = u'"return true" quality webapplications'
SITEURL = 'http://localhost:8000' #'http://return1.at'
#TWITTER_USERNAME = 'return1_at'

TIMEZONE = 'Europe/Vienna'

DEFAULT_LANG = 'en'

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/return1_at'),
    ('linkedin', 'http://at.linkedin.com/in/dominiquelederer'),
    ('xing', 'https://www.xing.com/profile/Dominique_Lederer'),
    ('github', 'https://github.com/return1'),
    ('about.me', 'https://about.me/dominique.lederer/'),
)

DEFAULT_PAGINATION = 50

THEME = "themes/return1"

STATIC_PATHS = ['images', 'assets', 'sandbox']

LOCALE = 'en_US.UTF-8'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

SUMMARY_MAX_LENGTH = 30

# A list of files to copy from the source to the destination
EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
}
#    (
#    ('assets/robots.txt', 'robots.txt'),
#    ('assets/favicon.ico', 'favicon.ico'),
#)

READERS = {'html': None} # see https://github.com/getpelican/pelican/issues/1157

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'

#seo
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

#PLUGINS = ['minify']
PLUGINS = []
