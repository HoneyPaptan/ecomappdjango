
from django.urls import path
from .views import register_page, login_page,activate_email,logout_page
urlpatterns = [
    path("register/", register_page, name="register"),
    path("login/", login_page, name="login"),
    path("logout/", logout_page, name="logout"),
    path("activate/<email_token>/", activate_email, name="activate_email"),
]
