"""my_luffy_permission URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from web import views as web_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', web_view.login,name="login"),
    path('user/add', web_view.user_add,name="user_add"),
    path('user/update', web_view.user_update,name="user_update"),
    path('user/delete', web_view.user_delete,name="user_delete"),
    path('user/list', web_view.user_list,name="user_list"),
    path('lesson/add', web_view.lesson_add,name="lesson_add"),
    path('lesson/update', web_view.lesson_update,name="lesson_update"),
    path('lesson/delete', web_view.lesson_delete,name="lesson_delete"),
    path('lesson/list', web_view.lesson_list,name="lesson_list"),

    path('')
]
