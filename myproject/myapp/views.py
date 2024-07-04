from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm,OwnerCreationForm,EmployeeCreationForm
from .models import Owner, Company,Employee
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request, 'home.html')

def signup_selection(request):
    return render(request, 'signup_selection.html')

from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import CustomUserCreationForm, OwnerCreationForm, EmployeeCreationForm

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        user_form = CustomUserCreationForm()
        owner_form = OwnerCreationForm()
        employee_form = EmployeeCreationForm()
        return render(request, 'registration/register.html', {
            'user_form': user_form,
            'owner_form': owner_form,
            'employee_form': employee_form
        })

    def post(self, request, *args, **kwargs):
        user_type = request.POST.get('user_type')
        user_form = CustomUserCreationForm(request.POST, request.FILES)
        
        if user_type == 'owner':
            owner_form = OwnerCreationForm(request.POST, request.FILES)
            if user_form.is_valid() and owner_form.is_valid():
                user = user_form.save(commit=False)
                user.is_owner = True
                user.save()
                
                company_name = owner_form.cleaned_data['company_name']
                company, created = Company.objects.get_or_create(company=company_name)
                owner = Owner(owner_id=user, company_id=company)
                owner.save()
                return redirect('register')  # Replace with your success URL
            else:
                employee_form = EmployeeCreationForm()
        else:
            employee_form = EmployeeCreationForm(request.POST, request.FILES)
            if user_form.is_valid() and employee_form.is_valid():
                user = user_form.save(commit=False)
                user.is_employee = True
                user.save()
                
                employee = employee_form.save(commit=False)
                employee.emp_id = user
                employee.company_id = employee_form.cleaned_data['owner_id'].company_id
                employee.save()
                return redirect('register')  # Replace with your success URL
            else:
                owner_form = OwnerCreationForm()

        return render(request, 'registration/register.html', {
            'user_form': user_form,
            'owner_form': owner_form,
            'employee_form': employee_form
        })

    

class OwnerRegisterView(CreateView):
    model = Owner
    form_class = OwnerCreationForm
    template_name = "registration/registerOwner.html"
    success_url = reverse_lazy("register")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'user_form' not in context:
            context['user_form'] = CustomUserCreationForm()
        if 'owner_form' not in context:
            context['owner_form'] = OwnerCreationForm()
        return context

    def form_valid(self, form):
        user_form = CustomUserCreationForm(self.request.POST,self.request.FILES)
        owner_form = form  # Use the form instance passed to the method
        print('IN validation')
                # Print POST data for debugging
        print("POST data:", self.request.POST)
        print("User form valid:", user_form.is_valid())
        print("Owner form valid:", owner_form.is_valid())
        if user_form.is_valid() and owner_form.is_valid():
            print('CREATING')
            user = user_form.save(commit=False)  # Save the user
            user.is_owner=True
            user.save()
            
            company_name = owner_form.cleaned_data['company_name']
            company, created = Company.objects.get_or_create(company=company_name)
            owner = Owner(owner_id=user, company_id=company)
            owner.save()
            return redirect(self.success_url)
        else:
            print("Form is invalid!")
            print(user_form.errors)
            print(owner_form.errors)
            context = self.get_context_data(form=form, user_form=user_form, owner_form=owner_form)
            return self.render_to_response(context)


    
class EmployeeRegisterView(CreateView):
    model = Employee
    form_class = EmployeeCreationForm
    template_name = "registration/registerEmployee.html"
    success_url = reverse_lazy("register")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'user_form' not in context:
            context['user_form'] = CustomUserCreationForm()
        if 'employee_form' not in context:
            context['employee_form'] = EmployeeCreationForm()
        return context

    def form_valid(self, form):
        user_form = CustomUserCreationForm(self.request.POST, self.request.FILES)
        employee_form = form  # Use the form instance passed to the method
        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save(commit=False)  # Save the user without committing to allow further modifications
            user.is_employee = True  # Assuming you have an is_employee field to indicate employee role
            user.save()
            employee = employee_form.save(commit=False)
            employee.emp_id = user
            employee.company_id = employee_form.cleaned_data['owner_id'].company_id
            employee.save()
            return redirect(self.success_url)
        else:
            context = self.get_context_data(form=form, user_form=user_form, employee_form=employee_form)
            return self.render_to_response(context)
