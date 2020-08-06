"""app01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views_tem
# from . import views
from cookie import  views
from session import  views as session_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url('add_book/', views_tem.add_book),
    # url('get_book/', views_tem.get_book),
    # url('delete_book/', views_tem.delete_book),
    # url('update_book/', views_tem.update_book),
    # url('add_book_double/', views_tem.add_book_double),
    # url('get_book_double/', views_tem.get_book_double),
    # url('aggregate/', views_tem.aggregates),
    # url('add_emp/',views.add_emp),

    url('login/', views.login),
    url(r'^index/', views.index),
    url('logout/', views.logout),
    url('order/', views.order),

    url('session_login/', session_views.s_login),
    url(r'^s_index/', session_views.s_index),
    url('s_logout/', session_views.s_logout),
]
