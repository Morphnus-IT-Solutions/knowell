from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'web.views.home', name='home'),
     url(r'^welcome/$', 'web.views.welcome', name='welcome'),
     url(r'^student-registration/$', 'students.views.student_registration', name='student-registration'),
    # url(r'^knowell/', include('knowell.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/media/images/favicon.ico'}))

from django.conf import settings
#if settings.DEBUG:
urlpatterns += patterns('',(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}) )
urlpatterns += patterns('',(r'^adminmedia/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_PREFIX}) )
