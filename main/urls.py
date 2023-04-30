from django.contrib import admin
from django.urls import path
from .views import home
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.log_in, name='login'),
    path('about/', views.about_us, name='about'),
    path('logout/', views.log_out, name='logout'),
    path('myprofile/', views.show_profile, name='profile'),
    path('myprofile/post/', views.post, name='post'),
    path('image/<int:image_id>/', views.img_view, name='image_view'), #Provisional view to generate a url to render images in HTML
]