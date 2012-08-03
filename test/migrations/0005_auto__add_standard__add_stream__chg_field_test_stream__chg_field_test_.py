# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Standard'
        db.create_table('test_standard', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('standard', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('test', ['Standard'])

        # Adding model 'Stream'
        db.create_table('test_stream', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stream', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('test', ['Stream'])


        # Changing field 'Test.stream'
        db.alter_column('test_test', 'stream_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['test.Stream'], null=True))

        # Changing field 'Test.standard'
        db.alter_column('test_test', 'standard_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['test.Standard']))

    def backwards(self, orm):
        # Deleting model 'Standard'
        db.delete_table('test_standard')

        # Deleting model 'Stream'
        db.delete_table('test_stream')


        # Changing field 'Test.stream'
        db.alter_column('test_test', 'stream_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['students.Stream'], null=True))

        # Changing field 'Test.standard'
        db.alter_column('test_test', 'standard_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['students.Standard']))

    models = {
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
        },
        'test.testsections': {
            'Meta': {'object_name': 'TestSections'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level_of_difficulty': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.LevelOfDifficulty']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.Section']"}),
            'section_score': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.Test']"}),
            'total_questions': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['test']