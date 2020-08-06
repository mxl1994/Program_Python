# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from . import models

# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    username = request.POST.get("username")
    password = request.POST.get("pwd")

    user_obj = models.UserInfo.objects.filter(username=username,password=password).first()
    print user_obj.username

    if not user_obj:
        return redirect("/login/")
    else:
        rep = redirect("/sindex/")
        rep.set_cookie("is_login",True)
        return rep

def index(request):
    print request.COOKIES.get('is_login')
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/login/')
    return render(request,"index.html")

def logout(request):
    rep = redirect('/login/')
    rep.delete_cookie("is_login")
    return rep

def order(request):
    print request.COOKIES.get('is_login')
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/login/')
    return render(request,"order.html")