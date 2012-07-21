# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Student.email'
        db.alter_column('students_student', 'email', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Student.phone_number'
        db.alter_column('students_student', 'phone_number', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Student.address'
        db.alter_column('students_student', 'address', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'Student.email'
        db.alter_column('students_student', 'email', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Student.phone_number'
        db.alter_column('students_student', 'phone_number', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Student.address'
        db.alter_column('students_student', 'address', self.gf('django.db.models.fields.TextField')(default=''))

    models = {
        'students.standard': {
            'Meta': {'object_name': 'Standard'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'standard': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'students.stream': {
            'Meta': {'object_name': 'Stream'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stream': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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
            'standard': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['students.Standard']"}),
            'stream': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['students.Stream']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['students']