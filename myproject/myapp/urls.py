# myapp/urls.py

from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Replace with your signup view and URL
   
]
