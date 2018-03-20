# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import itertools
import logging
import os
from shutil import copyfile
from pelican.generators import ArticlesGenerator
from pelican.generators import PagesGenerator
from pelican.settings import DEFAULT_CONFIG
from pelican import signals

from PIL import Image


th_size = [350, 250]

logger = logging.getLogger(__name__)


def initialized(pelican):

    p = os.path.expanduser('~/Pictures')

    DEFAULT_CONFIG.setdefault('PHOTO_LIBRARY', p)

    if pelican:
        pelican.settings.setdefault('PHOTO_LIBRARY', p)


def attach_clipper(x):
    return x[9:] if x[9] == '/' else x[8:]


def process_image(generator, content, image):
    if image.startswith('{attach}'):
        image = attach_clipper(image)
        path = os.path.join(generator.settings.get('PATH'), content.relative_dir, image)
        if os.path.isfile(path):

            if content.slug:
                out_dir = os.path.join(generator.settings.get('HEADERS_FOLDER'), content.slug)

            else:
                out_dir = os.path.join(generator.settings.get('HEADERS_FOLDER'), content.relative_dir)

            output_path = os.path.join(generator.output_path, out_dir)

            if not os.path.exists(output_path):
                os.makedirs(output_path)

            output_image_path = os.path.join(output_path, image)

            if not os.path.isfile(output_image_path):
                copyfile(path, output_image_path)

            # Resize thumbnail for lists of posts:
            th_name = ''.join(image.split('.')[:-1]) + '_r.jpg'
            th_full_path = os.path.join(output_path, th_name)
            if not os.path.isfile(th_full_path):
                im = Image.open(path)
                im.thumbnail((th_size[0], th_size[1]), Image.ANTIALIAS)
                im.save(th_full_path)

            content.header_image = os.path.join(out_dir, image)
            content.header_image_small = os.path.join(out_dir, th_name)
        else:
             logger.error('photo: No photo for {} at {}'.format(content.source_path, path))


def detect_header(generator, content):
    image = content.metadata.get('header', None)
    if image:
        if image.startswith('{attach}'):
            process_image(generator, content, image)
        else:
            logger.error('Header Image: Tag not recognized: {}'.format(image))


def detect_image_header(generators):
    """ Runs generator on both pages and articles."""
    for generator in generators:
        if isinstance(generator, ArticlesGenerator):
            for article in itertools.chain(generator.articles, generator.translations, generator.drafts):
                detect_header(generator, article)
        elif isinstance(generator, PagesGenerator):
            for page in itertools.chain(generator.pages, generator.translations, generator.hidden_pages):
                detect_header(generator, page)


def register():
    """Uses the new style of registration based on GitHub Pelican issue #314."""
    signals.initialized.connect(initialized)
    try:
        # signals.content_object_init.connect(detect_content)
        signals.all_generators_finalized.connect(detect_image_header)
        # signals.article_writer_finalized.connect(resize_photos)
    except Exception as e:
        print(e)