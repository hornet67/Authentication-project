from django.urls import path
from .views import *


urlpatterns = [
    path('', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('forget_password/', ForgetPasswordView.as_view(), name='forget_password'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    path('practice/', PracticeView.as_view(), name='practice'),
    
]
