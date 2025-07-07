from django.contrib import admin
from django.urls import path
from .views.auth_view import user_logout
from .views.auth_view import renderRegisterForm,renderLoginForm
from .views.home_view import renderHomePage

urlpatterns=[
    path('register',renderRegisterForm),
    path('login',renderLoginForm),
    path('',renderHomePage),
    path('logout/', user_logout, name='logout'),
]