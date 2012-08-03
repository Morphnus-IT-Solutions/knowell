from django.db import models
from storage import upload_storage
from imagekit.models import ImageModel
from south.modelsinspector import add_introspection_rules
from tinymce.models import HTMLField
from decimal import Decimal

add_introspection_rules([],["^tinymce\.models\.HTMLField"])

# Create your models here.
class Standard(models.Model):
    standard = models.CharField(max_length=20)

    def __unicode__(self):
        return self.standard

class Stream(models.Model):
    stream = models.CharField(max_length=20)
    def __unicode__(self):
        return self.stream
    

class LevelOfDifficulty(models.Model):
    level = models.CharField(max_length=10, unique=True)

    def __unicode__(self):
        return self.level


class SectionGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class Section(models.Model):
    class Meta:
        unique_together = ('name', 'type',)
    name = models.CharField(max_length=50)
    group = models.ForeignKey(SectionGroup)
    type = models.CharField(max_length=25, choices=(
            ('mcq', 'MCQ'),
            ('personality', 'Personality'),
        ),
        default = 'mcq', db_index=True)

    def __unicode__(self):
        return self.name


class Test(models.Model):
    title = models.CharField(max_length=30)
    description = HTMLField()
    marks = models.IntegerField(max_length=3)
    time = models.IntegerField(max_length=3, verbose_name="Time (in minutes)", blank=True, null=True)
    standard = models.ForeignKey(Standard)
    stream = models.ForeignKey(Stream, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title


class TestSection(models.Model):
    test = models.ForeignKey(Test)
    section = models.ForeignKey(Section)
    level_of_difficulty = models.ForeignKey(LevelOfDifficulty)
    total_questions = models.IntegerField(max_length=3)
    time = models.IntegerField(max_length=3, verbose_name="Time (in minutes)", default=Decimal('0'))
    section_score = models.IntegerField(max_length=3, blank=True, null=True, default=Decimal('0'))
