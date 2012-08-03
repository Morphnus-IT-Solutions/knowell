from django.db import models

from storage import upload_storage
from imagekit.models import ImageModel

from test.models import Section, LevelOfDifficulty

# Create your models here.

class Question(ImageModel):
    question = models.TextField()
    section = models.ForeignKey(Section)
    level_of_difficulty = models.ForeignKey(LevelOfDifficulty)
    image = models.ImageField(upload_to='question/%Y/%m', storage=upload_storage,blank=True,null=True)
    score = models.IntegerField(max_length=3, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.question


class Option(models.Model):
    question = models.ForeignKey(Question)
    option = models.CharField(max_length=50)
    is_correct = models.BooleanField(default=False)
    characteristics = models.CharField(max_length=100, null=True, blank=True)
    score = models.IntegerField(max_length=3, null=True, blank=True)

    def __unicode__(self):
        return "%s - %s" %(self.option, self.question)


class Characteristics(models.Model):
    question = models.ForeignKey(Question)
    characteristics = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s - %s" %(self.characteristics, self.question)
