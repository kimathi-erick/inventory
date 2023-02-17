from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.core.exceptions import ValidationError

class reg(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("a user with this email already exist")
        return email        
class productform(forms.ModelForm):
    class Meta:
        model=  Product 
        fields = '__all__'  

class profileupdate(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','phone','image']
class userupdate(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email'] 

class orderform(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product','order_quantity']


