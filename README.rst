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

```python
if not os.environ.has_key('DATABASE_URL'):
    os.environ['DATABASE_URL'] = '< your database url here >'
    MEDIA_ROOT = '< abs path to your local media root >'
    STATIC_ROOT = ''
    STATIC_URL = '/static/'
else:
    DEFAULT_FILE_STORAGE = 'shopcraft.s3utils.MediaRootS3BotoStorage'
    STATICFILES_STORAGE = 'shopcraft.s3utils.StaticRootS3BotoStorage'
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
    MEDIA_ROOT = ''
    STATIC_ROOT = '/static/'
    STATIC_URL = '//%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME
    MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

DATABASES = {'default': dj_database_url.config(default=os.environ['DATABASE_URL'])}
```

AND

s3utils.py is `here <https://gist.github.com/knarfytrebil/6937524>`

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