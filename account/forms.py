from .models import Useraccount
from django import forms

class UseraccountForm(forms.ModelForm):
    class Meta:
        model = Useraccount
        fields = ['username', 'password', 'email']
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Useraccount.objects.filter(username = username).exists():
            raise forms.ValidationError("Username already exists in database")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Useraccount.objects.filter(email = email).exists():
            raise forms.ValidationError("Email already exists in database")
        return email
    
    def save(self, commit=True):
        """Save the user with hashed password"""
        user = super().save(commit=False)
        # Hash the password before saving
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user