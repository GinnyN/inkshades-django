# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Obra'
        db.create_table(u'front_obra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['front.Author'])),
            ('resume', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.CharField')(default='Continuada', max_length=20)),
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'front', ['Obra'])

        # Adding M2M table for field tags on 'Obra'
        m2m_table_name = db.shorten_name(u'front_obra_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('obra', models.ForeignKey(orm[u'front.obra'], null=False)),
            ('tagobra', models.ForeignKey(orm[u'front.tagobra'], null=False))
        ))
        db.create_unique(m2m_table_name, ['obra_id', 'tagobra_id'])

        # Adding model 'Chapter'
        db.create_table(u'front_chapter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('resume', self.gf('django.db.models.fields.TextField')()),
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('obra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['front.Obra'])),
        ))
        db.send_create_signal(u'front', ['Chapter'])

        # Adding model 'TagObra'
        db.create_table(u'front_tagobra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'front', ['TagObra'])


    def backwards(self, orm):
        # Deleting model 'Obra'
        db.delete_table(u'front_obra')

        # Removing M2M table for field tags on 'Obra'
        db.delete_table(db.shorten_name(u'front_obra_tags'))

        # Deleting model 'Chapter'
        db.delete_table(u'front_chapter')

        # Deleting model 'TagObra'
        db.delete_table(u'front_tagobra')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'front.afiliate': {
            'Meta': {'object_name': 'Afiliate'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'front.author': {
            'Meta': {'object_name': 'Author'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'bio': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'front.chapter': {
            'Meta': {'object_name': 'Chapter'},
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obra': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['front.Obra']"}),
            'resume': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'front.obra': {
            'Meta': {'object_name': 'Obra'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['front.Author']"}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resume': ('django.db.models.fields.TextField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Continuada'", 'max_length': '20'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['front.TagObra']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'front.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['front.Author']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spotlight': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'spotlight_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'front.publicity': {
            'Meta': {'object_name': 'Publicity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'front.setting': {
            'Meta': {'object_name': 'Setting'},
            'deviantart': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subcultura': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'tumblr': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        },
        u'front.tagobra': {
            'Meta': {'object_name': 'TagObra'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['front']