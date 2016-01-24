from django.conf.urls import url
from . import views
from user_reg.views import delete_event

urlpatterns = [
    url(r'^$', views.index_page, name='index_page'),
    url(r'^dashboard/home/', views.dashboard, name='dashboard'),
    url(r'^dashboard/welcome/', views.welcome, name='welcome'),
    url(r'^dashboard/profile/', views.profile, name='profile'),
    url(r'^dashboard/events/', views.add_event, name='events'),
    url(r'^dashboard/delete/event/(?P<pk>\d+)/$', views.delete_event.as_view(), name='delete_event'), 
    url(r'^dashboard/tasks/', views.tasks, name='tasks'),
    url(r'^dashboard/guests/', views.guests, name='guests'),
    url(r'^dashboard/budgets/', views.budgets, name='budgets'),
    url(r'^dashboard/vendors/', views.vendors, name='vendors'),
    url(r'^dashboard/reviews/', views.reviews, name='reviews'),
    url(r'^dashboard/inbox/', views.inbox, name='inbox'),
]

