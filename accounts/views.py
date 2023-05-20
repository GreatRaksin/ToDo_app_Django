from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import UserRegisterForm


# Create your views here.
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

            return redirect('sign_in')
    return render(request, 'form.html', {'form': form, 'title': 'Регистрация'})

