from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns

handler400='views.handler404'

urlpatterns = [
    # Examples:
    # url(r'^$', 'mep_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('user_reg.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^contact/', include('contact_form.urls')),
]

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )