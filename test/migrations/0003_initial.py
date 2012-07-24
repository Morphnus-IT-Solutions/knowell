# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LevelOfDifficulty'
        db.create_table('test_levelofdifficulty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
        ))
        db.send_create_signal('test', ['LevelOfDifficulty'])

        # Adding model 'SectionGroup'
        db.create_table('test_sectiongroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('test', ['SectionGroup'])

        # Adding model 'Section'
        db.create_table('test_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['test.SectionGroup'])),
            ('type', self.gf('django.db.models.fields.CharField')(default='mcq', max_length=25, db_index=True)),
        ))
        db.send_create_signal('test', ['Section'])

        # Adding unique constraint on 'Section', fields ['name', 'type']
        db.create_unique('test_section', ['name', 'type'])

        # Adding model 'Test'
        db.create_table('test_test', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('tinymce.models.HTMLField')()),
            ('marks', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('time', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('standard', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['students.Standard'])),
            ('stream', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['students.Stream'], null=True, blank=True)),
        ))
        db.send_create_signal('test', ['Test'])

        # Adding model 'TestSections'
        db.create_table('test_testsections', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['test.Test'])),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['test.Section'])),
            ('level_of_difficulty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['test.LevelOfDifficulty'])),
            ('total_questions', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
        ))
        db.send_create_signal('test', ['TestSections'])


    def backwards(self, orm):
        # Removing unique constraint on 'Section', fields ['name', 'type']
        db.delete_unique('test_section', ['name', 'type'])

        # Deleting model 'LevelOfDifficulty'
        db.delete_table('test_levelofdifficulty')

        # Deleting model 'SectionGroup'
        db.delete_table('test_sectiongroup')

        # Deleting model 'Section'
        db.delete_table('test_section')

        # Deleting model 'Test'
        db.delete_table('test_test')

        # Deleting model 'TestSections'
        db.delete_table('test_testsections')


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
        'test.test': {
            'Meta': {'object_name': 'Test'},
            'description': ('tinymce.models.HTMLField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marks': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'standard': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['students.Standard']"}),
            'stream': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['students.Stream']", 'null': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'test.testsections': {
            'Meta': {'object_name': 'TestSections'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level_of_difficulty': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.LevelOfDifficulty']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.Section']"}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.Test']"}),
            'total_questions': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['test']