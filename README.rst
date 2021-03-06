Django FileBrowser
==================

**Stand-alone Media-Management ported from Grappelli-filebrowser, that works with S3 and django-suit**.

The FileBrowser is an extension to the `Django <http://www.djangoproject.com>`_ administration interface in order to:

* browse directories on your server and upload/delete/edit/rename files.
* include images/documents to your models/database using the ``FileBrowseField``.
* select images/documents with TinyMCE.

Requirements
------------

FileBrowser 3.5 requires

* Django > 1.4 (http://www.djangoproject.com)
* PIL with jpeg support


Porting Notes
-------------
Anyone trying to use this filebrowser with S3 must use the settings as follows:

settings.py is `here <https://gist.github.com/knarfytrebil/6937677>`_

AND

s3utils.py is `here <https://gist.github.com/knarfytrebil/6937524>`_

Documentation
-------------

http://readthedocs.org/docs/django-filebrowser/

Translation
-----------

https://www.transifex.com/projects/p/django-filebrowser/

Releases
--------

* FileBrowser 3.5.3 (Development Version, not yet released, see Branch Stable/3.5.x)
* FileBrowser 3.5.2 (February 22 2013): Compatible with Django 1.4/1.5
* FileBrowser 3.4.3 (April 2012): Compatible with Django 1.3

Older versions are availabe at GitHub, but are not supported anymore.