from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from django.contrib.sessions.models import Session 
from django.urls import reverse_lazy 
from .models import Useraccount

from .forms import UseraccountForm


# Create your views here.

#def Signup(request):
#   return render(request, 'signup.html')

class SignupView(CreateView):
    model = Useraccount
    form_class = UseraccountForm
    template_name = "signup.html"
    success_url = reverse_lazy('login') 


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
    
    
