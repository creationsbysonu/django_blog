from django.contrib import admin
from django.urls import path
from .views import renderRegisterForm,renderLoginForm,renderHomePage

urlpatterns=[
    path('register',renderRegisterForm),
    path('login',renderLoginForm),
    path('',renderHomePage)
]