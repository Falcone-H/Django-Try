#-*- coding = utf-8 -*-
#@Time : 2020/10/19 20:34
# 路由配置
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]