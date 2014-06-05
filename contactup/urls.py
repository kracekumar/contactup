from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'contactup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'new/$', 'contacts.views.new_contact', name='new_contact'),
    url(r'edit/(?P<contact_id>\d+)/$', 'contacts.views.edit_contact', name='edit_contact'),
    url(r'delete/(?P<contact_id>\d+)/$', 'contacts.views.delete_contact', name='delete_contact'),

    url(r'^', 'contacts.views.index', name="index"),
)
