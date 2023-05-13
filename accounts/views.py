from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegisterForm


# Create your views here.
def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():  # если форма отправлена без ошибок
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None and not user.is_staff:  # если юзер не админ
            login(request, user)  # "входим" пользователя в личный кабинет
            return redirect('index')  # вернуть пользователя на главную
    return render(request, "form.html", {"form": form, "title": "Войти"})


def logout_view(request):
    logout(request)  # "выходим" пользователя
    return redirect('index')  # возвращаем на главную страницу


def register_view(request):
    form = UserRegisterForm(request.POST)
    if form.is_valid():
        password = form.cleaned_data['password']
        password_confirm = form.cleaned_data['confirm_password']
        if password == password_confirm:
            user = form.save(commit=False)  # добавляю пользователя в БД, но не сохраняю изменения
            user.set_password(password)
            user.save()  # .save(commit=True) сохранить изменения в базе данных

            return redirect('login')
    return render(request, 'form.html', {'form': form, 'title': 'Регистрация'})

