from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from django.contrib.sessions.models import Session 
from django.urls import reverse_lazy 
from .models import Useraccount
from django.contrib import messages 
from django.shortcuts import redirect

from .forms import UseraccountForm


# Create your views here.

#def Signup(request):
#   return render(request, 'signup.html')

class SignupView(CreateView):
    model = Useraccount
    form_class = UseraccountForm
    template_name = "signup.html"
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Account created successfully.")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # Messages for form errors (optional - Django already shows errors on form)
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return super().form_invalid(form)
        
class LoginView(TemplateView):
    template_name = "login.html"

class ForgetPasswordView(TemplateView):
    template_name = "forget_password.html"

class ResetPasswordView(TemplateView):
    template_name = "reset_password.html"
    
class PracticeView(ListView):
    
    model = Useraccount
    template_name = "practice.html"
    context_object_name = "users"
    
    
