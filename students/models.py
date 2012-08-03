from django.db import models
from storage import upload_storage
from imagekit.models import ImageModel
from south.modelsinspector import add_introspection_rules
from tinymce.models import HTMLField
from decimal import Decimal

from test.models import Test, Section, Standard, Stream
from question.models import Question, Option
# Create your models here.

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
    phone_number = models.CharField(max_length=30, default='')
    email = models.CharField(max_length=200, default='')
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    pincode = models.IntegerField(max_length=6, blank=True, null=True)
    guardian_name = models.CharField(max_length=30, blank=True, null=True)
    guardian_contact_number = models.CharField(max_length=30, blank=True, null=True)
    career_aspiration_1 = models.CharField(max_length=50, blank=True, null=True, verbose_name="1.")
    career_aspiration_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="2.")
    career_aspiration_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="3.")


class StudentTest(models.Model):
    student = models.ForeignKey(Student)
    test = models.ForeignKey(Test)
    created_on = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    total_score = models.IntegerField(max_length=3)
    score_acquired = models.IntegerField(max_length=3, blank=True, null=True)


class StudentTestSectionDetail(models.Model):
    studenttest = models.ForeignKey(StudentTest)
    section = models.ForeignKey(Section)
    time = models.IntegerField(max_length=3, verbose_name="Time (in minutes)", default=Decimal('0')) 
    score = models.IntegerField(max_length=3, default=Decimal('0'))

class StudentTestDetail(models.Model):
    studenttest = models.ForeignKey(StudentTest)
    question = models.ForeignKey(Question)
    question_score = models.IntegerField(max_length=3, blank=True, null=True)
    correct_answer = models.CharField(max_length=100, blank=True, null=True)
    answer = models.CharField(max_length=100, blank=True, null=True)
    answer_score = models.IntegerField(max_length=3, blank=True, null=True)
