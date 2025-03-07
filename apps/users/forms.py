from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(UserChangeForm):
    password = None  # Oculta la opción de cambiar contraseña en este formulario

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_image', 'bio', 'phone_number']
