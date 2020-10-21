from django.contrib import admin
from .models import Question, Choice

# username:admin
# password:admin
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']




admin.site.register(Question, QuestionAdmin) # 注册操作，告诉admin站点，将polls的模型加入站点内，接受管理

