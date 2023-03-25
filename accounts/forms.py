from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):  # создаю свою форму на основе формы из Django
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))  # виджет будет превращать весь текст в звездочки

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')  # очистим данные из формы от лишних пробелов и мета-информации
        password = self.cleaned_data.get('password')

        if username and password:  # if bool(username) == True and bool(password) == True (если поля не пустые)
            user = authenticate(username=username, password=password)
            if not user:  # если не получилось авторизовать пользователя в системе
                raise forms.ValidationError('Такого пользователя не существует или пароль неправильный!')
            if not user.is_active():  # если аккаунт пользователя отключен администратором
                raise forms.ValidationError('Ваш аккаунт был забанен. Бот.')
        return super(UserLoginForm, self).clean()  # формируем форму логина заново


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
