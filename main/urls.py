from django.contrib import admin
from django.urls import path
from .views import home
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.log_in, name='login'),
]