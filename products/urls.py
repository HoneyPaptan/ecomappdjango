
from django.contrib import admin
from django.urls import path,include
from  . import views


urlpatterns = [
    path('', views.productsPage, name="Productpage"),
    path("product/<slug:slug>", views.productView, name="Productview" ),
 
    

   
    
    
]