# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table('web_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('tinymce.models.HTMLField')()),
            ('page', self.gf('django.db.models.fields.CharField')(default='welcome', unique=True, max_length=25, db_index=True)),
        ))
        db.send_create_signal('web', ['Page'])

        # Adding field 'Banner.type'
        db.add_column('web_banner', 'type',
                      self.gf('django.db.models.fields.CharField')(default='home', max_length=25, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table('web_page')

        # Deleting field 'Banner.type'
        db.delete_column('web_banner', 'type')


    models = {
        'web.banner': {
            'Meta': {'object_name': 'Banner'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'home'", 'max_length': '25', 'db_index': 'True'})
        },
        'web.page': {
            'Meta': {'object_name': 'Page'},
            'description': ('tinymce.models.HTMLField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.CharField', [], {'default': "'welcome'", 'unique': 'True', 'max_length': '25', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['web']