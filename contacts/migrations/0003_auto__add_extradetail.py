# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ExtraDetail'
        db.create_table(u'contacts_extradetail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Person'])),
            ('website', self.gf('django.db.models.fields.URLField')(default=u'', max_length=200)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True)),
            ('relationship', self.gf('django.db.models.fields.CharField')(default=u'', max_length=100)),
        ))
        db.send_create_signal(u'contacts', ['ExtraDetail'])


    def backwards(self, orm):
        # Deleting model 'ExtraDetail'
        db.delete_table(u'contacts_extradetail')


    models = {
        u'contacts.extradetail': {
            'Meta': {'object_name': 'ExtraDetail'},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Person']"}),
            'relationship': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100'}),
            'website': ('django.db.models.fields.URLField', [], {'default': "u''", 'max_length': '200'})
        },
        u'contacts.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "u''", 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['contacts']