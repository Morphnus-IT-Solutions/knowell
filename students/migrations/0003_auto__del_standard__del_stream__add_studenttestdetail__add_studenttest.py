# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Standard'
        db.delete_table('students_standard')

        # Deleting model 'Stream'
        db.delete_table('students_stream')

        # Adding model 'StudentTestDetail'
        db.create_table('students_studenttestdetail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('studenttest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['students.StudentTest'])),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['test.Section'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['question.Question'])),
            ('correct_answer', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True, blank=True)),
        ))
        db.send_create_signal('students', ['StudentTestDetail'])

        # Adding model 'StudentTest'
        db.create_table('students_studenttest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['students.Student'])),
            ('test', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['test.Test'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('started_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ended_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('test_score', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('score_acquired', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True, blank=True)),
        ))
        db.send_create_signal('students', ['StudentTest'])


        # Changing field 'Student.stream'
        db.alter_column('students_student', 'stream_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['test.Stream'], null=True))

        # Changing field 'Student.standard'
        db.alter_column('students_student', 'standard_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['test.Standard']))

    def backwards(self, orm):
        # Adding model 'Standard'
        db.create_table('students_standard', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('standard', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('students', ['Standard'])

        # Adding model 'Stream'
        db.create_table('students_stream', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stream', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('students', ['Stream'])

        # Deleting model 'StudentTestDetail'
        db.delete_table('students_studenttestdetail')

        # Deleting model 'StudentTest'
        db.delete_table('students_studenttest')


        # Changing field 'Student.stream'
        db.alter_column('students_student', 'stream_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['students.Stream'], null=True))

        # Changing field 'Student.standard'
        db.alter_column('students_student', 'standard_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['students.Standard']))

    models = {
        'question.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'level_of_difficulty': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.LevelOfDifficulty']"}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'score': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.Section']"})
        },
        'students.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'career_aspiration_1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'career_aspiration_2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'career_aspiration_3': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'education_institution': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'male'", 'max_length': '15', 'db_index': 'True'}),
            'guardian_contact_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'guardian_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_exam_appeared': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'marks_expected_actual': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'pincode': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'registration_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'standard': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.Standard']"}),
            'stream': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.Stream']", 'null': 'True', 'blank': 'True'})
        },
        'students.studenttest': {
            'Meta': {'object_name': 'StudentTest'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ended_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score_acquired': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['students.Student']"}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.Test']"}),
            'test_score': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'students.studenttestdetail': {
            'Meta': {'object_name': 'StudentTestDetail'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'correct_answer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['question.Question']"}),
            'score': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.Section']"}),
            'studenttest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['students.StudentTest']"})
        },
        'test.levelofdifficulty': {
            'Meta': {'object_name': 'LevelOfDifficulty'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'})
        },
        'test.section': {
            'Meta': {'unique_together': "(('name', 'type'),)", 'object_name': 'Section'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.SectionGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'mcq'", 'max_length': '25', 'db_index': 'True'})
        },
        'test.sectiongroup': {
            'Meta': {'object_name': 'SectionGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'test.standard': {
            'Meta': {'object_name': 'Standard'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'standard': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'test.stream': {
            'Meta': {'object_name': 'Stream'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stream': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'test.test': {
            'Meta': {'object_name': 'Test'},
            'description': ('tinymce.models.HTMLField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marks': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'standard': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.Standard']"}),
            'stream': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.Stream']", 'null': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['students']