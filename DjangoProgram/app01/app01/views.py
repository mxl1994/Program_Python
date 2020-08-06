# -*- coding:utf-8 -*-

from django.shortcuts import render,HttpResponse
from app01.My_Forms import EmpForm
from app01 import models
from django.core.exceptions import ValidationError

def add_emp(request):
    if request.method == "GET":
        form = EmpForm()
        return  render(request,"add_emp.html",{"form":form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data.pop("r_salary")
            models.Emp.objects.create(**data)
            # return HttpResponse("ok")
            # return render(request, "add_emp.html", {"form": form})
            return redirect("/index/")
        else:
            clean_errors = form.errors.get("__all__")   #获取全局钩子错误信息
        return render(request,"add_emp.html", {"form": form, "clean_errors": clean_errors})

from django.contrib.auth.models import User
User.objects.create(username='runboo',password='123')