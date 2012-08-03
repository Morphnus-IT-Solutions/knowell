# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TestSection.time'
        db.add_column('test_testsection', 'time',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=3),
                      keep_default=True)


        # Changing field 'Test.time'
        db.alter_column('test_test', 'time', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True))

    def backwards(self, orm):
        # Deleting field 'TestSection.time'
        db.delete_column('test_testsection', 'time')


        # Changing field 'Test.time'
        db.alter_column('test_test', 'time', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=3))

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
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'marks': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'standard': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.Standard']"}),
            'stream': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.Stream']", 'null': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'test.testsection': {
            'Meta': {'object_name': 'TestSection'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level_of_difficulty': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.LevelOfDifficulty']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.Section']"}),
            'section_score': ('django.db.models.fields.IntegerField', [], {'default': "'0'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.Test']"}),
            'time': ('django.db.models.fields.IntegerField', [], {'default': "'0'", 'max_length': '3'}),
            'total_questions': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['test']
