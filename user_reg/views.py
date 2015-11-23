from django.shortcuts import render

def index_page(request):
    return render(request, 'user_reg/index.html', {})
    
def member_reg(request):
    return render(request, 'user_reg/members.html', {})
    
def vendor_reg(request):
    return render(request, 'user_reg/vendors.html', {})
