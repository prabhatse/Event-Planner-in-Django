from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns
from user_reg import views

handler400='views.handler404'

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('user_reg.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^contact/', include('contact_form.urls')),
    url(r'^vendors/success/', views.vendors_success, name='vendors_success'),
    url(r'^vendors/', views.vendors_reg, name='vendors_reg'),
]

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )