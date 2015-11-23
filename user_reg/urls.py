from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_page, name='index_page'),
    url(r'^members', views.member_login, name='member_login'),
    url(r'^vendors', views.vendor_login, name='vendor_login'),
]
