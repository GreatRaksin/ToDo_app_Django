from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):  # создаем форму регистрации по МОДЕЛИ
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username'}
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Email'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password (again)'}))

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password',
        ]  # те поля, которые будут отображаться в форме регистрации
