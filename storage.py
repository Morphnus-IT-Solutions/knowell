from django.core.files.storage import FileSystemStorage
from django.conf import settings

class UploadStorage(FileSystemStorage):

    def __init__(self, location=settings.UPLOAD_ROOT, base_url='/images'):
        super(UploadStorage, self).__init__(location=location, base_url=base_url)

    def url(self, name):
        p = super(UploadStorage, self).url(name)
        return p

upload_storage = UploadStorage(location=settings.UPLOAD_ROOT, base_url='/images')
