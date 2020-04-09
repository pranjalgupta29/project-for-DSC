from .import views
from django.urls import path

urlpatterns = [
    path('about/', views.about,name='blog-about'),
    path('',views.home,name='blog-home'),
]
