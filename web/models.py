# Create your models here.

from django.db import models
from storage import upload_storage
from imagekit.models import ImageModel

class Banner(ImageModel):
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to='banner/%Y/%m', storage=upload_storage,blank=True,null=True)
