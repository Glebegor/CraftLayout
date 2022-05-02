from telnetlib import LOGOUT
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth import views as authViews
from .views import profile, RegisterPage, AvatarPage, BannerPage, ChangeProfPage
urlpatterns = [
    path('changeBanner/', BannerPage, name="changeBanner"),
    path('changeProfile/', ChangeProfPage, name="changeProfile"),
    path('changeAvatar/', AvatarPage, name="changeAvatar"),
    path('reg/', RegisterPage, name='reg'),
    path('profile/', profile, name='profile'),
    path('login/', authViews.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit')
]
