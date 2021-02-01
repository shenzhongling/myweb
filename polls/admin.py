from django.contrib import admin

from polls.models import Question, Choice


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1  # 添加选项数量


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('问题标题', {'fields': ['question_text']}),
        ('日期信息', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]  # 添加选项
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # 管理界面显示列内容
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_per_page = 10


admin.site.register(Question, QuestionAdmin)
