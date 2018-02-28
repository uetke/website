#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Aquiles Carattino'
SITENAME = 'Uetke'
SITEURL = 'uetke.com'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'
DEFAULT_DATE = 'fs'

DEFAULT_PAGINATION = 10
INDEX_SAVE_AS = 'blog/index.html'
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'template/uetke'

TEMPLATE_PAGES = {'static_pages/courses.html': 'courses/index.html',
                  'static_pages/pythonforthelab.html': 'courses/pythonlab/index.html',
                  'static_pages/advancedpythonforthelab.html': 'courses/advanced/index.html',
                  'static_pages/gitforscientists.html': 'courses/gitscience/index.html',
                  'static_pages/contact.html': 'contact/index.html',
                  'static_pages/register.html': 'courses/register/index.html',
                  'static_pages/register_thanks.html': 'courses/register/thanks/index.html',
                  'static_pages/privacy.html': 'privacy/index.html',
                  'static_pages/about_us.html': 'about-us/index.html',
                  'static_pages/main.html': 'index.html',}

MINIFY = {
  'remove_comments': True,
  'remove_all_empty_space': True,
  'remove_optional_attribute_quotes': False
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = ['minify', 'excercises_directive', 'images', 'header_image', 'sitemap']

ARTICLE_URL = 'blog/{category}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{category}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

STATIC_PATHS = ['images', 'pages', 'projects', 'blog']
LOAD_CONTENT_CACHE = False
USE_FOLDER_AS_CATEGORY = True

SITEMAP = {
    'format': 'xml',
    'exclude': ['archives.html', 'tags.html', 'category/', 'author/', 'tag/', 'categories.html']
}