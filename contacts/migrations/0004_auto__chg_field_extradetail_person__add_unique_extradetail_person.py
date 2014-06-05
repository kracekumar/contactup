# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ExtraDetail.person'
        db.alter_column(u'contacts_extradetail', 'person_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contacts.Person'], unique=True))
        # Adding unique constraint on 'ExtraDetail', fields ['person']
        db.create_unique(u'contacts_extradetail', ['person_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ExtraDetail', fields ['person']
        db.delete_unique(u'contacts_extradetail', ['person_id'])


        # Changing field 'ExtraDetail.person'
        db.alter_column(u'contacts_extradetail', 'person_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Person']))

    models = {
        u'contacts.extradetail': {
            'Meta': {'object_name': 'ExtraDetail'},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'person': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contacts.Person']", 'unique': 'True'}),
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