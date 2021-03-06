from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import databrowse

from django.contrib import admin
admin.autodiscover()


from treemap.custom_admin import editor
from registration.views import register

urlpatterns = patterns('',
    (r'^_admin_/', include(admin.site.urls)),
    (r'^editor/(.*)', editor.root),
    (r'^databrowse/(.*)', databrowse.site.root),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DATA}),
    (r'^Species/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.MEDIA_ROOT + "/Species"}),
    (r'^Nodes/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.MEDIA_ROOT + "/Nodes"}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),   
    (r'^admin_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.ADMIN_MEDIA_ROOT}), 
    (r'^comments/', include('django.contrib.comments.urls')), 

    (r'^', include('treemap.urls')),
    (r'^', include('qs_tiles.urls')),

    # using new 0.8 beta with "backends" support
    # http://docs.b-list.org/django-registration/0.8/
    # override just the /register view to customize form and save actions...
    url(r'^accounts/register/$',register,
       { 'backend': 'registration_backend.TreeBackend' },
       name='registration_register'),
    # dispatch the remainder of the urls to the default backend...
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^profiles/', include('profiles.urls')),
    (r'^treekey/', include('treekey.urls'))

)
