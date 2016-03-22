from django.conf.urls import url
from . import views

urlpatterns = [
    #Front-End
    url(r'^$', views.index_page, name='index_page'),
    #url(r'^vendors', views.add_vendor, name='add_vendor'),
    #Dashboard Home/Welcome
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
    url(r'^dashboard/guests/invitations/', views.add_invitation, name='invitations'),
    # *** Guests Home ***
    url(r'^dashboard/guests/', views.guests, name='guests'),
    #Budgets
    # *** Budget Items ***
    url(r'^dashboard/budgets/view/delete-item/(?P<pk>\d+)/$', views.DeleteBudgetItem.as_view(), name='delete_budget_item'),
    url(r'^dashboard/budgets/view/edit-item/(?P<pk>\d+)/$', views.EditBudgetItem.as_view(), name='edit_budget_item'),
    url(r'^dashboard/budgets/view/add-item', views.add_budget_item, name='add_budget_item'),
    # *** Individual budgets ***
    url(r'^dashboard/budgets/view/(?P<pk>\d+)/$', views.ViewBudget.as_view(), name='view_budget'),
    url(r'^dashboard/budgets/delete/(?P<pk>\d+)/$', views.DeleteBudget.as_view(), name='delete_budget'),
    url(r'^dashboard/budgets/edit/(?P<pk>\d+)/$', views.EditBudget.as_view(), name='edit_budget'),
    url(r'^dashboard/budgets/', views.add_budget, name='budgets'),
    #Vendors
    url(r'^dashboard/vendors/view/(?P<pk>\d+)/$', views.ViewVendor.as_view(), name='vendors_single'),
    url(r'^dashboard/vendors/beauty-wellness', views.vendors_beauty, name='vendors_beauty'),
    url(r'^dashboard/vendors/flowers-decor', views.vendors_decor, name='vendors_decor'),
    url(r'^dashboard/vendors/clothing-accessories', views.vendors_clothing, name='vendors_clothing'),
    url(r'^dashboard/vendors/music-entertainment', views.vendors_entertainment, name='vendors_entertainment'),
    url(r'^dashboard/vendors/photography-videography', views.vendors_photography, name='vendors_photography'),
    url(r'^dashboard/vendors/food-drinks', views.vendors_food, name='vendors_food'),
    url(r'^dashboard/vendors/cake-pastries-desserts', views.vendors_cake, name='vendors_cake'),
    url(r'^dashboard/vendors/stationery', views.vendors_stationery, name='vendors_stationery'),
    url(r'^dashboard/vendors/gifts-favours', views.vendors_favours, name='vendors_favours'),
    url(r'^dashboard/vendors/transport', views.vendors_transport, name='vendors_transport'),
    url(r'^dashboard/vendors/venue', views.vendors_venue, name='vendors_venue'),
    url(r'^dashboard/vendors/other', views.vendors_other, name='vendors_other'),
    url(r'^dashboard/vendors/', views.vendors, name='vendors'),
    #Reviews
    url(r'^dashboard/reviews/add', views.add_review, name='add_review'),
    url(r'^dashboard/reviews/', views.reviews, name='reviews'),
]


