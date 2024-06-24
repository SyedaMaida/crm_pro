# from django.shortcuts import render,redirect
# from django.contrib.auth.models import User,auth
# from django.contrib import messages
# from .models import Account


from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"

    def form_invalid(self, form):
        print("Form is invalid!")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

# Create your views here.
# def register(request):
#     if request.method=='POST':
#         name=request.POST['name']
#         userID=request.POST['userID']
#         phone=request.POST['phone']
#         email=request.POST['email']
#         password=request.POST['password']
#         cpassword=request.POST['cpassword']
#         company=request.POST['company']
#         industry=request.POST['industry']
#         noEmp=request.POST['noEmp']
#         role=request.POST['role']

#         if not all([name, userID, email, password, phone, company, industry, noEmp, role]):
#             messages.error(request, 'Please fill out all fields')
#             return render(request, 'register.html')        
#         if Account.objects.filter(userID=userID).exists():
#             messages.info(request,'UserID Already Used')
#             return redirect ('register')
#         if Account.objects.filter(email=email).exists():
#             messages.info(request,'UserID Already Used')
#             return redirect ('register')
        
#         if password==cpassword:
#             user=Account.objects.create_user(name=name,userID=userID,phone=phone,email=email,password=password,companyName=company,industry=industry,noEmp=noEmp,role=role)   #the argumentds username,email etc are retrieved from the POST request data submitted by the user
#             user.save()
#             return redirect('login')
#         else:
#             messages.info(request,'Password does not match')
#             return redirect('register')
#     return render(request,'register.html')
        