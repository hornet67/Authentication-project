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
    
    def post(self, request, *args, **kwargs):
        form = UseraccountForm(request.POST)
        if form.is_valid():
            # Use the form's save method which already has password hashing
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect('login')
        else:
            # Show specific error messages from the form
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            messages.error(request, "Please correct the errors below.")
        return render(request, self.template_name, {'form': form})
        
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
    
    
