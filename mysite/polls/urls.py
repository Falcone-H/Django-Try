#-*- coding = utf-8 -*-
#@Time : 2020/10/19 20:34
# 路由配置
from django.urls import path
from . import views


app_name = 'polls'      # 使用URLconf的命名空间

urlpatterns = [
    path('', views.IndexView.as_view(), name='inedx'),  # /polls/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),  # /polls/question_id/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),  # /polls/question_id/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),    # /polls/question_id/vote/
]