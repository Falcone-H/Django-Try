# 路由文件
# 所有的任务都是从这里开始分配，相当于Django驱动站点的目录
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
# include语法相当于多级路由
# 它把接收到的url地址去除与此匹配的部分，将剩下的字符串传递给下一级路由urlconf进行判断

# path()方法可以接受4个参数，其中前两个必须是：route和view，以及两个可选的参数：kwargs和name
# 1、route是一个匹配URL的准则。当Django响应一个请求时，它会从urlpatterns的第一项path开始，按顺序依次匹配列表中的项，直到找到匹配的项。
#   然后执行该条目映射的视图函数或下级路由，其后的条目将不再继续匹配。
#   因此，url路由执行的是短路机制，要注意path的编写顺序
# 2、view指的是处理当前url请求的视图函数。
#   当Django匹配到某个路由条目时，自动封装的HttpRequest对象作为第一个参数，被“捕获”的参数以关键字参数的形式，传递给该条目指定的视图view
# 3、kwargs 任意数量的关键字参数可以作为一个字典传递给目标视图。
# 4、name 对URL进行命名，让你能够在Django的任意处，尤其时模板内显示地引用它。
#   相当于给URL取了个全局变量名。