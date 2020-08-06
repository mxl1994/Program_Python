# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from cookie import models

# Create your views here.
def s_login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("pwd")

    user_obj = models.UserInfo.objects.filter(username=username, password=password).first()
    print(user_obj.username)

    if not user_obj:
        return redirect("/session_login/")
    else:
        request.session['is_login'] = True
        request.session['user1'] = username
        return redirect("/s_index/")


def s_index(request):
    status = request.session.get('is_login')
    if not status:
        return redirect('/session_login/')
    return render(request, "s_index.html")


def s_logout(request):
   # del request.session["is_login"] # 删除session_data里的一组键值对
    request.session.flush() # 删除一条记录包括(session_key session_data expire_date)三个字段
    return redirect('/session_login/')