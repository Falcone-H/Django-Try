from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

# 修改模型时的操作分为三步：
# 1、在models.py中修改模型
# 2、运行 python manage.py makemigrations 为改动创建迁移记录文件
# 3、运行 python manage.py migrate 将操作同步到数据库

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):  # 方便在shell中打印对象
        return self.question_text
    def was_published_recently(self):   # 是否在最近发布的问卷
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):  # 方便在shell中打印对象
        return self.choice_text