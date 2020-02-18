from django.shortcuts import render, redirect
from django.http import HttpResponse
from rbac.models import *
from rbac.service.permission import init_permission


# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    user_name = request.POST['user_name']
    password = request.POST['password']
    user = UserInfo.objects.get(name=user_name, password=password)
    if user is None:
        return redirect(request, 'login.html', {'mag': '用户名或密码错误'})

    init_permission(user, request)

    return HttpResponse("...")


def user_add(request):
    return HttpResponse('user add')


def user_update(request):
    return HttpResponse('user update')


def user_delete(request):
    return HttpResponse('user delete')


def user_list(request):
    return HttpResponse('user_list')


def lesson_add(request):
    return HttpResponse('lesson_add')


def lesson_update(request):
    return HttpResponse('lesson_update')


def lesson_delete(request):
    return HttpResponse('lesson_delete')


def lesson_list(request):
    return HttpResponse('lesson_list')

