from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from. models import ShopCart

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'last Name'}),
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'password1': forms.TextInput(attrs={'class':'form-control'}),
            'password2': forms.TextInput(attrs={'class':'form-control'}),
        }

class ShopCartForm(forms.ModelForm):
    class Meta: 
        models = ShopCart
        fields = ('quantity',)