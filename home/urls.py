
from django.contrib import admin
from django.urls import path,include
from  . import views


urlpatterns = [
    path('', views.homePage, name="Homepage"),
    path('about/', views.aboutPage, name="Aboutpage"),
    path('contact/', views.contactPage, name="Contactpage"),
    path("products/", include("products.urls")),
   
    

   
    
    
]