# myapp/urls.py

from django.urls import path
from .views import RegisterView,OwnerRegisterView,EmployeeRegisterView
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup_selection, name='signup_selection'),
    path('registerOwner/',OwnerRegisterView.as_view(), name='registerOwner'),
    path('registerEmployee/',EmployeeRegisterView.as_view(), name='registerEmployee'),
    path('register/', RegisterView.as_view(), name='register'),  # Replace with your signup view and URL
   
]
