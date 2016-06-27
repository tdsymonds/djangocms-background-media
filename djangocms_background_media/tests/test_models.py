# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.files import File

from cms.test_utils.testcases import CMSTestCase
from filer.models import Image as FilerImage

from ..models import BackgroundMedia


class BackgroundMediaTest(CMSTestCase):
    def setUp(self):
        self.f = FilerImage.objects.create(original_filename='test',
            file=File(open('djangocms_background_media/tests/media/bg.jpg')))

    def test_creating_model(self):
        b = BackgroundMedia.objects.create(name='test', image=self.f)
        b.save()

        all_background_media = BackgroundMedia.objects.all()

        self.assertEqual(all_background_media.count(), 1)
        self.assertEqual(all_background_media[0], b)
        self.assertEqual(b.__str__(), b.name)

    def test_has_video(self):
        b = BackgroundMedia.objects.create(name='test', image=self.f)
        self.assertFalse(b.has_video())
