from django.contrib import admin
from .models import Question

# username:admin
# password:admin
# Register your models here.
admin.site.register(Question) # 注册操作，告诉admin站点，将polls的模型加入站点内，接受管理
