# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import BackgroundMedia


class BackgroundMediaPlugin(CMSPluginBase):
    name = _('Background Media')
    module = _('DjangoCMS Background Media')
    model = BackgroundMedia
    render_template = 'djangocms_bg_media/_bg.html'
    cache = False
    allow_children = True

plugin_pool.register_plugin(BackgroundMediaPlugin)
