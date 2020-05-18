from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, FileInput, Select, EmailInput

from home.models import UserProfile
from product.models import Product


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Adresi'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Adı'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyadı'})

        }
CITY = [
    ('Istanbul','Istanbul'),
    ('Ankara','Ankara'),
    ('Izmir','Izmir'),
]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('university', 'department', 'grade', 'city', 'image')
        widgets = {
            'university': TextInput(attrs={'class': 'form-control', 'placeholder': 'university'}),
            'department': TextInput(attrs={'class': 'form-control', 'placeholder': 'department'}),
            'grade': TextInput(attrs={'class': 'form-control', 'placeholder': 'class'}),
            'city': Select(attrs={'class': 'form-control', 'placeholder': 'city'}, choices=CITY),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'image'}),

        }




