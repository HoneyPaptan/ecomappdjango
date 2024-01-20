from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')
def products(request):
    return render(request, 'products/products.html')
def proddetail(request):
    return render(request, 'products/proddetail.html')
def register_page(request):
    return render(request, 'accounts/register.html')
def login_page(request):
    return render(request, 'accounts/login.html')
def adress_page(request):
    return render(request, 'accounts/address.html')