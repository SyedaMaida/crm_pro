from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    cpassword = models.CharField(max_length=128)
    company = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    noEmp = models.BigIntegerField()
    role = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True,default=None)
    phone = models.CharField(max_length=20)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'company', 'industry', 'noEmp', 'role', 'name', 'phone']

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email  # Set a default username (using email as an example)
        super().save(*args, **kwargs)
