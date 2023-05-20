"""ToDo_app_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import register_view, logout_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),  # подключаю файл с путями к главному приложению
    path('login/', auth_views.LoginView.as_view(template_name='login.html',
                                                redirect_authenticated_user=True,
                                                extra_context={"title": "Login"}), name='sign_in'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='sign_up'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # подключаю URL-адреса медиа к сайту
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = 'ToDo Information System'
admin.site.site_title = 'В админ панель ToDo'
admin.site.index_title = 'Добро пожаловать в интерфейс администратора'