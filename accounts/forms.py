from django import forms
from django.contrib.auth import authenticate, login, logout, get_user_model

User = get_user_model()  # создали экземпляр класса User, который есть Django


class UserLoginForm(forms.Form):  # создаю свою форму на основе формы из Django
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)  # виджет будет превращать весь текст в звездочки

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
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password',
        ]  # те поля, которые будут отображаться в форме регистрации
