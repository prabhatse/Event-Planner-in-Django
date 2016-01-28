from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from user_reg.forms import *
from user_reg.models import *
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy

#Dashboard Home/Welcome

def index_page(request):
    return render(request, 'user_reg/index.html', {})

# *** Home ***
def home(request):
    return render(request, 'dashboard/dashboard.html', {})

# *** Profile Add ***
def welcome(request):
    if request.method == 'POST':
        member_form = MemberForm(data=request.POST)
        if member_form.is_valid():
            member = member_form.save(commit=False)
            member.user = request.user
            if 'image' in request.FILES:
                member.image = request.FILES['image']
            member.save()
            return HttpResponseRedirect('/dashboard/profile') # Redirect after POST
        else:
            print member_form.errors
    else:
        member_form = MemberForm()
    return render(request, 'dashboard/welcome.html', {'member_form': member_form})

#User Profile

# *** Profile Edit & Display ***
def profile(request):
    member = get_object_or_404(Member, user=request.user)
    if request.method == "POST":
        edit_form = MemberForm(request.POST, instance=member)
        if edit_form.is_valid():
            member = edit_form.save(commit=False)
            member.user = request.user
            if 'image' in request.FILES:
                member.image = request.FILES['image']
            member.save()
            return HttpResponseRedirect('/dashboard/profile')
    else:
        edit_form = MemberForm(instance=member)
    context_dict = { 'member': member, 'edit_form': edit_form }
    return render(request, 'dashboard/profile.html', context_dict)

# *** Inbox ***
def inbox(request):
    return render(request, 'dashboard/inbox.html', {})

#Events

# *** Add & Display ***
def add_event(request):
    events = Event.objects.filter(host=request.user)
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.host = request.user
            event.save()
            return HttpResponseRedirect('/dashboard/events') # Redirect after POST
        else:
            print event_form.errors
    else:
        event_form = EventForm()
    context_dict = { 'events': events, 'event_form': event_form}
    return render(request, 'dashboard/events.html', context_dict)

# *** Delete ***
class delete_event(DeleteView):
    model = Event
    success_url = reverse_lazy('events')
    template_name = 'dashboard/event_delete.html'

    def get_event(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        event = super(delete_event, self).get_event()
        if not event.host == self.request.user:
            raise Http404
        return event

# *** Edit ***
class edit_event(UpdateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events')
    template_name = 'dashboard/event_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(edit_event, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(edit_event, self).post(request, *args, **kwargs)
#Tasks

def tasks(request):
    return render(request, 'dashboard/tasks.html', {})

#Guests

# *** Guests Home ***
def guests(request):
    return render(request, 'dashboard/guests.html', {})

# *** Guestlists ***

# *** Add & Display ***
def add_guestlist(request):
    guestlists = Guestlist.objects.filter(host=request.user)
    if request.method == 'POST':
        guestlist_form = GuestlistForm(request.POST)
        if guestlist_form.is_valid():
            guestlist = guestlist_form.save(commit=False)
            guestlist.host = request.user
            guestlist.save()
            return HttpResponseRedirect('/dashboard/guests/guestlists') # Redirect after POST
        else:
            print guestlist_form.errors
    else:
        guestlist_form = GuestlistForm()
    context_dict = { 'guestlists': guestlists, 'guestlist_form': guestlist_form}
    return render(request, 'dashboard/guestlists.html', context_dict)

# *** Delete ***
class delete_guestlist(DeleteView):
    model = Guestlist
    success_url = reverse_lazy('guestlists')
    template_name = 'dashboard/guestlist_delete.html'

    def get_guestlist(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        guestlist = super(delete_guestlist, self).get_guestlist()
        if not guestlist.host == self.request.user:
            raise Http404
        return guestlist

# *** Edit ***
class edit_guestlist(UpdateView):
    model = Guestlist
    form_class = GuestlistForm
    success_url = reverse_lazy('guestlists')
    template_name = 'dashboard/guestlist_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(edit_guestlist, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(edit_guestlist, self).post(request, *args, **kwargs)

# *** Profiles ***

# *** Add ***
def add_guest(request):
    guests = Guest.objects.filter(host=request.user)
    if request.method == 'POST':
        guest_form = GuestForm(request.POST)
        if guest_form.is_valid():
            guest = guest_form.save(commit=False)
            guest.host = request.user
            guest.save()
            return HttpResponseRedirect('/dashboard/guests/profiles') # Redirect after POST
        else:
            print guest_form.errors
    else:
        guest_form = GuestForm()
    context_dict = { 'guests': guests, 'guest_form': guest_form}
    return render(request, 'dashboard/guest_add.html', context_dict)

# *** Display ***
def guest_profiles(request):
    guests = Guest.objects.filter(host=request.user)
    context_dict = { 'guests': guests}
    return render(request, 'dashboard/guest_profiles.html', context_dict)

# *** Delete ***
class delete_guest(DeleteView):
    model = Guest
    success_url = reverse_lazy('guest_profiles')
    template_name = 'dashboard/guest_delete.html'

    def get_guest(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        guest = super(delete_guest, self).get_guest()
        if not guest.host == self.request.user:
            raise Http404
        return guest

# *** Edit ***
class edit_guest(UpdateView):
    model = Guest
    form_class = GuestForm
    success_url = reverse_lazy('guest_profiles')
    template_name = 'dashboard/guest_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(edit_guest, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(edit_guest, self).post(request, *args, **kwargs)

# *** Invitations ***
def invitations(request):
    return render(request, 'dashboard/guests2.html', {})

#Budgets

def budgets(request):
    return render(request, 'dashboard/budgets.html', {})

#Vendors

def vendors(request):
    return render(request, 'dashboard/vendors.html', {})

#Reviews 

def reviews(request):
    return render(request, 'dashboard/reviews.html', {})


   

