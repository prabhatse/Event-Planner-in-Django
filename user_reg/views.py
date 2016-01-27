from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from user_reg.forms import *
from user_reg.models import *
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy

def index_page(request):
    return render(request, 'user_reg/index.html', {})

def dashboard(request):
    return render(request, 'dashboard/dashboard.html', {})

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

def tasks(request):
    return render(request, 'dashboard/tasks.html', {})

#def guests(request):
#    return render(request, 'dashboard/guests.html', {})

def add_guestlist(request):
    guestlists = Guestlist.objects.filter(host=request.user)
    if request.method == 'POST':
        guestlist_form = GuestlistForm(request.POST)
        if guestlist_form.is_valid():
            guestlist = guestlist_form.save(commit=False)
            guestlist.host = request.user
            guestlist.save()
            return HttpResponseRedirect('/dashboard/guests') # Redirect after POST
        else:
            print guestlist_form.errors
    else:
        guestlist_form = GuestlistForm()
    context_dict = { 'guestlists': guestlists, 'guestlist_form': guestlist_form}
    return render(request, 'dashboard/guestlists.html', context_dict)

class delete_guestlist(DeleteView):
    model = Guestlist
    success_url = reverse_lazy('guestlists')
    template_name = 'dashboard/guestlist_delete.html'

    def get_guestlist(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        guestlist = super(delete_guestlist, self).get_event()
        if not guestlist.host == self.request.user:
            raise Http404
        return guestlist

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

def budgets(request):
    return render(request, 'dashboard/budgets.html', {})

def vendors(request):
    return render(request, 'dashboard/vendors.html', {})

def reviews(request):
    return render(request, 'dashboard/reviews.html', {})

def inbox(request):
    return render(request, 'dashboard/inbox.html', {})
   

