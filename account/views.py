from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Useraccount


# Create your views here.

#def Signup(request):
#   return render(request, 'signup.html')

class SignupView(TemplateView):
    template_name = "signup.html"

def Login(request):
    return render(request, 'login.html')

class LoginView(TemplateView):
    template_name = "login.html"

class ForgetPasswordView(TemplateView):
    template_name = "forget_password.html"

class ResetPasswordView(TemplateView):
    template_name = "reset_password.html"
    
class PracticeView(TemplateView):
    model = "Useraccount"
    template_name = "practice.html"
    context_object_name = "users"
