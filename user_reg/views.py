from django.shortcuts import render

def index_page(request):
    return render(request, 'user_reg/index.html', {})

def dashboard(request):
    return render(request, 'dashboard/dashboard.html', {})

def profile(request):
    return render(request, 'dashboard/profile.html', {})

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
   

