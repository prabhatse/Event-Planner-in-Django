from django.conf.urls import url
from . import views

urlpatterns = [
    #Dashboard Home/Welcome
    url(r'^$', views.index_page, name='index_page'),
    url(r'^dashboard/home/', views.home, name='home'),
    url(r'^dashboard/welcome/', views.welcome, name='welcome'),
    #User Profile
    url(r'^dashboard/profile/', views.profile, name='profile'),
    url(r'^dashboard/inbox/', views.inbox, name='inbox'),
    #Events
    url(r'^dashboard/events/delete/(?P<pk>\d+)/$', views.DeleteEvent.as_view(), name='delete_event'),
    url(r'^dashboard/events/edit/(?P<pk>\d+)/$', views.EditEvent.as_view(), name='edit_event'), 
    url(r'^dashboard/events/', views.add_event, name='events'),
    #Tasks
    url(r'^dashboard/tasks/delete/(?P<pk>\d+)/$', views.DeleteTask.as_view(), name='delete_task'),
    url(r'^dashboard/tasks/edit/(?P<pk>\d+)/$', views.EditTask.as_view(), name='edit_task'), 
    url(r'^dashboard/tasks/', views.add_task, name='tasks'),
    #Guests
    # *** Guestlists ***
    url(r'^dashboard/guests/guestlists/delete/(?P<pk>\d+)/$', views.DeleteGuestlist.as_view(), name='delete_guestlist'),
    url(r'^dashboard/guests/guestlists/edit/(?P<pk>\d+)/$', views.EditGuestlist.as_view(), name='edit_guestlist'),
    url(r'^dashboard/guests/guestlists/', views.add_guestlist, name='guestlists'),
    # *** Profiles ***
    url(r'^dashboard/guests/profiles/add', views.add_guest, name='add_guest'),
    url(r'^dashboard/guests/profiles/edit/(?P<pk>\d+)/$', views.EditGuest.as_view(), name='edit_guest'),
    url(r'^dashboard/guests/profiles/delete/(?P<pk>\d+)/$', views.DeleteGuest.as_view(), name='delete_guest'), 
    url(r'^dashboard/guests/profiles', views.guest_profiles, name='guest_profiles'),
    # *** Invitations ***
    url(r'^dashboard/guests/invitations/', views.invitations.as_view(), name='invitations'),
    # *** Guests Home ***
    url(r'^dashboard/guests/', views.guests, name='guests'),
    #Budgets
    url(r'^dashboard/budgets/view', views.view_budget, name='view_budget'),
    url(r'^dashboard/budgets/', views.add_budget, name='budgets'),
    #Vendors
    url(r'^dashboard/vendors/', views.vendors, name='vendors'),
    #Reviews
    url(r'^dashboard/reviews/', views.reviews, name='reviews'),
]

