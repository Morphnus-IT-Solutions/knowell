# Create your models here.

from django.db import models
from storage import upload_storage
from imagekit.models import ImageModel
from south.modelsinspector import add_introspection_rules
from tinymce.models import HTMLField

add_introspection_rules([],["^tinymce\.models\.HTMLField"])

class Banner(ImageModel):
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to='banner/%Y/%m', storage=upload_storage,blank=True,null=True)
    type = models.CharField(max_length=25, choices=(
        ('home', 'Home Page'),
        ('welcome', 'Welcome'),
        ('logo', 'Logo'),
    ),
    default = 'home', db_index=True)


class Page(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    image = models.ImageField(upload_to='page/%Y/%m', storage=upload_storage,blank=True,null=True)
    page = models.CharField(max_length=25, unique=True, choices=(
        ('home', 'Home Page'),
        ('welcome', 'Welcome'),
        ('student', 'Student Registration'),
    ),
    default = 'welcome', db_index=True)
