from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from .models import Profile
def register_page(request):
    if request.method =="POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_obj  = User.objects.filter(username= email)

        if user_obj.exists():
            messages.error(request, "user already exists")
            return HttpResponseRedirect(request.path_info)
        
      
        
        user_obj = User.objects.create(first_name = first_name, last_name = last_name, email=email,username = email)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, "an email has been sent to this mail, please verify your account")
        return  HttpResponseRedirect(request.path_info)



    return render(request, "accounts/register.html")



def login_page(request):
    if request.method =="POST":
       
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_obj  = User.objects.filter(username= email)

        if not user_obj.exists():
            messages.error(request, "Account not found")
            return HttpResponseRedirect(request.path_info)
        
        if not user_obj[0].profile.is_verified:
            messages.error(request, "verify your email")
            return HttpResponseRedirect(request.path_info)

      
        user_obj = authenticate(username = email, password = password)
        if user_obj:
            login(request, user_obj)
            return redirect("/")
        messages.error(request, "invalid credentials")
        return  HttpResponseRedirect(request.path_info)
    return render(request, "accounts/login.html")



def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token = email_token)
        user.is_verified = True
        user.save()
        return redirect("/")
    except Exception as e:
        
        return HttpResponse("invalid token")
    


def logout_page(request):
    
    logout(request)
    return redirect("/")
        
    