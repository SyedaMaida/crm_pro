# myapp/urls.py

from django.urls import path
from .views import RegisterView
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/', views.home, name='home'),
    path('register/', RegisterView.as_view(), name='register'),  # Replace with your signup view and URL
   
]
