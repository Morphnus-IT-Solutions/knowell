# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Section', fields ['name', 'type']
        db.delete_unique('tests_section', ['name', 'type'])

        # Deleting model 'LevelOfDifficulty'
        db.delete_table('tests_levelofdifficulty')

        # Deleting model 'Test'
        db.delete_table('tests_test')

        # Deleting model 'Section'
        db.delete_table('tests_section')

        # Deleting model 'TestSections'
        db.delete_table('tests_testsections')


    def backwards(self, orm):
        # Adding model 'LevelOfDifficulty'
        db.create_table('tests_levelofdifficulty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True)),
        ))
        db.send_create_signal('tests', ['LevelOfDifficulty'])

        # Adding model 'Test'
        db.create_table('tests_test', (
            ('description', self.gf('tinymce.models.HTMLField')()),
            ('stream', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['students.Stream'], null=True, blank=True)),
            ('marks', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('time', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('standard', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['students.Standard'])),
        ))
        db.send_create_signal('tests', ['Test'])

        # Adding model 'Section'
        db.create_table('tests_section', (
            ('type', self.gf('django.db.models.fields.CharField')(default='mcq', max_length=25, db_index=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('tests', ['Section'])

        # Adding unique constraint on 'Section', fields ['name', 'type']
        db.create_unique('tests_section', ['name', 'type'])

        # Adding model 'TestSections'
        db.create_table('tests_testsections', (
            ('total_questions', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tests.Section'])),
            ('level_of_difficulty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tests.LevelOfDifficulty'])),
            ('test', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tests.Test'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('tests', ['TestSections'])


    models = {
        
    }

    complete_apps = ['tests']