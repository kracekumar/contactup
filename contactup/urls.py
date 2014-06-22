from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'contactup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'contacts.views.logout_page', name='logout'),
    url(r'new/$', 'contacts.views.new_contact', name='new_contact'),
    url(r'edit/(?P<contact_id>\d+)/$', 'contacts.views.edit_contact', name='edit_contact'),
    url(r'delete/(?P<contact_id>\d+)/$', 'contacts.views.delete_contact', name='delete_contact'),
    url(r'(?P<character>^[a-zA-Z])/$', 'contacts.views.display_contacts_for_character', name='display_character_for_character'),

    url(r'^', 'contacts.views.index', name="index"),
)
