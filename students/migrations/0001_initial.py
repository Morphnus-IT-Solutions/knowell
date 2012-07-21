# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
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

        # Adding model 'Student'
        db.create_table('students_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, db_index=True)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('registration_number', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(default='male', max_length=15, db_index=True)),
            ('education_institution', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('standard', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['students.Standard'])),
            ('stream', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['students.Stream'], null=True, blank=True)),
            ('last_exam_appeared', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('marks_expected_actual', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('pincode', self.gf('django.db.models.fields.IntegerField')(max_length=6, null=True, blank=True)),
            ('guardian_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('guardian_contact_number', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('career_aspiration_1', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('career_aspiration_2', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('career_aspiration_3', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('students', ['Student'])


    def backwards(self, orm):
        # Deleting model 'Standard'
        db.delete_table('students_standard')

        # Deleting model 'Stream'
        db.delete_table('students_stream')

        # Deleting model 'Student'
        db.delete_table('students_student')


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
            'address': ('django.db.models.fields.TextField', [], {}),
            'career_aspiration_1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'career_aspiration_2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'career_aspiration_3': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'education_institution': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'male'", 'max_length': '15', 'db_index': 'True'}),
            'guardian_contact_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'guardian_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_exam_appeared': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'marks_expected_actual': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'pincode': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'registration_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'standard': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['students.Standard']"}),
            'stream': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['students.Stream']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['students']