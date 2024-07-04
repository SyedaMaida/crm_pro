from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    cpassword = models.CharField(max_length=128)
    full_name = models.CharField(max_length=100,blank=True,null=True,default=None)
    phone = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    # address = models.CharField(max_length=200,default=None,blank=True,null=True)
    is_owner = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name','email', 'phone']

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email  # Set a default username (using email as an example)
        super().save(*args, **kwargs)


# ----------------        Company       --------------------------------
class Company(models.Model):

    company_id=models.BigAutoField(primary_key=True,unique=True)
    company = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.company

# ----------------        OWNER        --------------------------------

class Owner(models.Model):

    username = models.CharField(max_length=100, unique=True,default=None)
    owner_id = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.username
    
# ----------------        Employee       --------------------------------

class Employee(models.Model):

    username = models.CharField(max_length=100, unique=True,default=None)
    emp_id = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    position = models.CharField(max_length=20)
    owner_id= models.ForeignKey(Owner, on_delete=models.CASCADE,default=None)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return self.emp_id.username

