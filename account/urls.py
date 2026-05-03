from django.urls import path
from .views import *


urlpatterns = [
    path('', Signup, name='signup'),
    path('login/', Login, name='login'),
    path('forget_password/', Forget_password, name='forget_password'),
    path('reset_password/', Reset_password, name='reset_password'), 
    
]