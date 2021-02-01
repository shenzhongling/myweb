import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField('问题', max_length=200)
    pub_date = models.DateTimeField('发布日期')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'  # 管理界面添加排序
    was_published_recently.boolean = True  # 管理界面添加彩色对错图标
    was_published_recently.short_description = '最近发布'  # 管理界面列标

    class meta:
        verbose_name = '问题'
        verbose_name_plural = '问题集'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
