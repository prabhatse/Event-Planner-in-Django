from django.shortcuts import render
from django.contrib.auth.models import User
from user_reg.forms import MemberForm
from user_reg.models import Member
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

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


def events(request):
    return render(request, 'dashboard/events.html', {})

def tasks(request):
    return render(request, 'dashboard/tasks.html', {})

def guests(request):
    return render(request, 'dashboard/guests.html', {})

def budgets(request):
    return render(request, 'dashboard/budgets.html', {})

def vendors(request):
    return render(request, 'dashboard/vendors.html', {})

def reviews(request):
    return render(request, 'dashboard/reviews.html', {})

def inbox(request):
    return render(request, 'dashboard/inbox.html', {})
   

