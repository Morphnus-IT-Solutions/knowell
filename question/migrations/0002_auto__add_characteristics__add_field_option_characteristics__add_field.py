# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Characteristics'
        db.create_table('question_characteristics', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['question.Question'])),
            ('characteristics', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('question', ['Characteristics'])

        # Adding field 'Option.characteristics'
        db.add_column('question_option', 'characteristics',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Option.score'
        db.add_column('question_option', 'score',
                      self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Characteristics'
        db.delete_table('question_characteristics')

        # Deleting field 'Option.characteristics'
        db.delete_column('question_option', 'characteristics')

        # Deleting field 'Option.score'
        db.delete_column('question_option', 'score')


    models = {
        'question.characteristics': {
            'Meta': {'object_name': 'Characteristics'},
            'characteristics': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['question.Question']"})
        },
        'question.option': {
            'Meta': {'object_name': 'Option'},
            'characteristics': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'option': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['question.Question']"}),
            'score': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
        },
        'question.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'level_of_difficulty': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.LevelOfDifficulty']"}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'score': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['test.Section']"})
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
        }
    }

    complete_apps = ['question']