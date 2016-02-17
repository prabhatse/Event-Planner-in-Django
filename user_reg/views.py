from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from user_reg.forms import *
from user_reg.models import *
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView

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
class DeleteEvent(DeleteView):
    model = Event
    success_url = reverse_lazy('events')
    template_name = 'dashboard/event_delete.html'

    def get_event(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        event = super(DeleteEvent, self).get_event()
        if not event.host == self.request.user:
            raise Http404
        return event

# *** Edit ***
class EditEvent(UpdateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events')
    template_name = 'dashboard/event_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(EditEvent, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(EditEvent, self).post(request, *args, **kwargs)

#Tasks

# *** Add & Display ***
def add_task(request):
    tasks = Task.objects.filter(host=request.user)
    User = host = request.user
    if request.method == 'POST':
        task_form = TaskForm(User, request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.host = request.user
            task.save()
            return HttpResponseRedirect('/dashboard/tasks') # Redirect after POST
        else:
            print task_form.errors
    else:
        task_form = TaskForm(User)
    context_dict = { 'tasks': tasks, 'task_form': task_form}
    return render(request, 'dashboard/tasks.html', context_dict)

# *** Delete ***
class DeleteTask(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    template_name = 'dashboard/task_delete.html'

    def get_task(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        task = super(DeleteTask, self).get_task()
        if not task.host == self.request.user:
            raise Http404
        return task

# *** Edit ***
class EditTask(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    template_name = 'dashboard/task_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(EditTask, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(EditTask, self).post(request, *args, **kwargs)

    def get_form_kwargs(self, **kwargs):
        kwargs = super(EditTask, self).get_form_kwargs(**kwargs)
        kwargs['host'] = self.request.user
        return kwargs

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
class DeleteGuestlist(DeleteView):
    model = Guestlist
    success_url = reverse_lazy('guestlists')
    template_name = 'dashboard/guestlist_delete.html'

    def get_guestlist(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        guestlist = super(DeleteGuestlist, self).get_guestlist()
        if not guestlist.host == self.request.user:
            raise Http404
        return guestlist

# *** Edit ***
class EditGuestlist(UpdateView):
    model = Guestlist
    form_class = GuestlistForm
    success_url = reverse_lazy('guestlists')
    template_name = 'dashboard/guestlist_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(EditGuestlist, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(EditGuestlist, self).post(request, *args, **kwargs)

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
class DeleteGuest(DeleteView):
    model = Guest
    success_url = reverse_lazy('guest_profiles')
    template_name = 'dashboard/guest_delete.html'

    def get_guest(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        guest = super(DeleteGuest, self).get_guest()
        if not guest.host == self.request.user:
            raise Http404
        return guest

# *** Edit ***
class EditGuest(UpdateView):
    model = Guest
    form_class = GuestForm
    success_url = reverse_lazy('guest_profiles')
    template_name = 'dashboard/guest_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(EditGuest, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(EditGuest, self).post(request, *args, **kwargs)

# *** Invitations ***
#def invitations(request):
 #   return render(request, 'dashboard/invitations.html', {})

class invitations(FormView):
    form_class = InvitationForm
    recipient_list = None
    template_name = 'dashboard/invitations.html'

    def form_valid(self, form):
        form.save()
        return super(invitations, self).form_valid(form)

    def get_form_kwargs(self):
        # ContactForm instances require instantiation with an
        # HttpRequest.
        kwargs = super(invitations, self).get_form_kwargs()
        kwargs.update({'request': self.request})

        # We may also have been given a recipient list when
        # instantiated.
        if self.recipient_list is not None:
            kwargs.update({'recipient_list': self.recipient_list})
        return kwargs

   # def get_success_url(self):
        # This is in a method instead of the success_url attribute
        # because doing it as an attribute would involve a
        # module-level call to reverse(), creating a circular
        # dependency between the URLConf (which imports this module)
        # and this module (which would need to access the URLConf to
        # make the reverse() call).
      #  return reverse('contact_form_sent')

#Budgets

#def budgets(request):
 #   return render(request, 'dashboard/budgets.html', {})

# *** Add & Display ***
def add_budget(request):
    budgets = Budget.objects.filter(owner=request.user)
    User = host = request.user
    if request.method == 'POST':
        budget_form = BudgetForm(User, request.POST)
        if budget_form.is_valid():
            budget = budget_form.save(commit=False)
            budget.owner = request.user
            budget.save()
            return HttpResponseRedirect('/dashboard/budgets') # Redirect after POST
        else:
            print task_form.errors
    else:
        budget_form = BudgetForm(User)
    context_dict = { 'budgets': budgets, 'budget_form': budget_form}
    return render(request, 'dashboard/budgets.html', context_dict)

# *** View Budget ***
def view_budget(request):
    budgets = Budget.objects.filter(owner=request.user)
    context_dict = { 'budgets': budgets}
    return render(request, 'dashboard/budget_view.html', context_dict)

#Vendors

def vendors(request):
    return render(request, 'dashboard/vendors.html', {})

#Reviews 

def reviews(request):
    return render(request, 'dashboard/reviews.html', {})

