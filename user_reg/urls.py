from django.conf.urls import url
from . import views
from user_reg.views import delete_event, edit_event

urlpatterns = [
    url(r'^$', views.index_page, name='index_page'),
    url(r'^dashboard/home/', views.dashboard, name='dashboard'),
    url(r'^dashboard/welcome/', views.welcome, name='welcome'),
    url(r'^dashboard/profile/', views.profile, name='profile'),
    url(r'^dashboard/events/delete/(?P<pk>\d+)/$', views.delete_event.as_view(), name='delete_event'),
    url(r'^dashboard/events/edit/(?P<pk>\d+)/$', views.edit_event.as_view(), name='edit_event'), 
    url(r'^dashboard/events/', views.add_event, name='events'),
    url(r'^dashboard/tasks/', views.tasks, name='tasks'),
    url(r'^dashboard/guestlists/delete/(?P<pk>\d+)/$', views.delete_guestlist.as_view(), name='delete_guestlist'),
    url(r'^dashboard/guestlists/edit/(?P<pk>\d+)/$', views.edit_guestlist.as_view(), name='edit_guestlist'),
    url(r'^dashboard/guestlists/', views.add_guestlist, name='guestlists'), 
    url(r'^dashboard/budgets/', views.budgets, name='budgets'),
    url(r'^dashboard/vendors/', views.vendors, name='vendors'),
    url(r'^dashboard/reviews/', views.reviews, name='reviews'),
    url(r'^dashboard/inbox/', views.inbox, name='inbox'),
]

