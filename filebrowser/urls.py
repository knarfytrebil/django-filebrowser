# As of version 3.4, all urls moved to FileBrowserSite class in filebrowser.sites
# This file will be removed with version 3.6
import os
from filebrowser.sites import FileBrowserSite
from filebrowser.storage import S3BotoStorageMixin
from shopcraft.s3utils import MediaRootS3BotoStorage
from django.core.files.storage import default_storage

storage = default_storage

if 'ON_HEROKU' in os.environ:
	s3storage = MediaRootS3BotoStorage()

	if S3BotoStorageMixin not in s3storage.__class__.__bases__:
		s3storage.__class__.__bases__ += (S3BotoStorageMixin,)
		storage = s3storage

site = FileBrowserSite(name='filebrowser', storage=default_storage)

urlpatterns = site.get_urls()