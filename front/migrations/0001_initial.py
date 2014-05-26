# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'front_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'front', ['Author'])

        # Adding model 'Post'
        db.create_table(u'front_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['front.Author'])),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'front', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'front_author')

        # Deleting model 'Post'
        db.delete_table(u'front_post')


    models = {
        u'front.author': {
            'Meta': {'object_name': 'Author'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'front.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['front.Author']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['front']