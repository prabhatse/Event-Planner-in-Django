from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from user_reg.forms import *
from user_reg.models import *
#from django.utils.functional import SimpleLazyObject

def context_processor(request):
    member = get_object_or_404(Member, user=request.user)
    events = Event.objects.filter(host=request.user)
    events_count = Event.objects.count()
    tasks = Task.objects.filter(host=request.user)
    tasks_count = Task.objects.count()
    guests = Guest.objects.filter(host=request.user)
    guests_count = Guest.objects.count()
    budgets = Budget.objects.filter(owner=request.user)
    budgets_count = Budget.objects.count()
    context_dict = {'member': member, 'events': events, 'events_count': events_count, 
    'tasks': tasks, 'tasks_count': tasks_count, 'guests': guests, 'guests_count': guests_count, 
    'budgets': budgets, 'budgets_count': budgets_count }
    return context_dict

'''

def context_processor(request):
    def my_query():
        member = get_object_or_404(Member, user=request.user)
        events = Event.objects.filter(host=request.user)
        events_count = Event.objects.count()
        tasks = Task.objects.filter(host=request.user)
        tasks_count = Task.objects.count()
        guests = Guest.objects.filter(host=request.user)
        guests_count = Guest.objects.count()
        budgets = Budget.objects.filter(owner=request.user)
        budgets_count = Budget.objects.count()
        context_dict = { 'member': member, 'events': events, 'events_count': events_count, 
        'tasks': tasks, 'tasks_count': tasks_count, 'guests': guests, 'guests_count': guests_count, 
        'budgets': budgets, 'budgets_count': budgets_count }
        return result
    return {
        'result': SimpleLazyObject(my_query)
    }
'''
