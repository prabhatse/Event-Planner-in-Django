from django.shortcuts import render

def index_page(request):
    return render(request, 'user_reg/index.html', {})
    
def member_login(request):
    return render(request, 'user_reg/members.html', {})