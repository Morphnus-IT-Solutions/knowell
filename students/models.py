from django.db import models
from storage import upload_storage
from imagekit.models import ImageModel
from south.modelsinspector import add_introspection_rules
from tinymce.models import HTMLField

# Create your models here.

class Standard(models.Model):
    standard = models.CharField(max_length=20)

class Stream(models.Model):
    stream = models.CharField(max_length=20)

class Student(models.Model):
    first_name = models.CharField(max_length=30, db_index=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    registration_number = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=15, db_index=True, default='male', 
                    choices=(
                        ('male', 'Male'),
                        ('female', 'Female')))
    education_institution = models.CharField(max_length=100, blank=True, null=True)
    standard = models.ForeignKey(Standard, db_index=True)
    stream = models.ForeignKey(Stream, blank=True, null=True)
    last_exam_appeared = models.CharField(max_length=100, blank=True, null=True)
    marks_expected_actual = models.CharField(max_length=100, blank=True, null=True, verbose_name="Marks (Expected/Actual)")
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    address = models.TextField()
    city = models.CharField(max_length=30, blank=True, null=True)
    pincode = models.IntegerField(max_length=6, blank=True, null=True)
    guardian_name = models.CharField(max_length=30, blank=True, null=True)
    guardian_contact_number = models.CharField(max_length=30, blank=True, null=True)
    career_aspiration_1 = models.CharField(max_length=50, blank=True, null=True, verbose_name="1.")
    career_aspiration_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="2.")
    career_aspiration_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="3.")
