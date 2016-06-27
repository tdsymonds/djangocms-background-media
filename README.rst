.. image:: https://travis-ci.org/tdsymonds/djangocms-background-media.svg?branch=master
    :target: https://travis-ci.org/tdsymonds/djangocms-background-media
.. image:: https://coveralls.io/repos/github/tdsymonds/djangocms-background-media/badge.svg?branch=master&t=1 :target: https://coveralls.io/github/tdsymonds/djangocms-background-media?branch=master 
.. image:: https://img.shields.io/badge/pypi-v1.0.0-blue.svg
    :target: https://github.com/tdsymonds/djangocms-background-media
.. image:: https://img.shields.io/badge/license-MIT%20License-red.svg
    :target: https://github.com/tdsymonds/djangocms-background-media

djangocms-background-media
==========================
This is a simple `django-cms`_ plugin that provides responsive, full screen background media with text. 

A HTML div container is added to the page that can either have a background image or video. Video backgrounds are enabled by making use of the `Vide`_ jQuery plugin. Child plugins are enabled, so text and/or hyperlinks etc can be placed on top of the background media, see usage below for more details.

Installation
------------
To install::

    pip install djangocms-background-media

Then add djangocms-background-media to your installed apps::

    INSTALLED_APPS = [
        ...
        'djangocms_background_media',
        ...
    ]

If you're not already using `django-filer`_ and `easy-thumbnails`_ then these too will need to be added to your installed apps::

    INSTALLED_APPS = [
        ...
        'easy_thumbnails',
        'filer',
        ...
    ]

And run the migrations::

    ./manage.py migrate

The package assume that jQuery has been added to the site already. So if you're not using, please add to you templates/base.html:

.. code:: html

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>

Usage
------
The background media plugin is added to a page and configured accordingly. If a background image is all that is required, then an image is uploaded, the container height can be updated, and optional overlay added and that's all. If a video background is required then a video is uploaded and a video poster should be provided, as this is what will be displayed for mobile browsers. You're also able to pass a JSON config object if you wish. More details of the video plugin can be viewed on `Vide`_. 

I have provided the ability to link an optional style sheet to the page, so that the plugin will work "out of the box", if you don't link the style sheet you will need to provide your own styling.

To add text, links or another plugin to the background media plugin, simply add the child plugins you desire. 



.. _django-cms: https://github.com/divio/django-cms
.. _django-filer: https://github.com/divio/django-filer
.. _easy-thumbnails: https://github.com/SmileyChris/easy-thumbnails
.. _Vide: http://vodkabears.github.io/vide/
