# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'contacts_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(default=u'', max_length=100)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('address', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'contacts', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'contacts_person')


    models = {
        u'contacts.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['contacts']