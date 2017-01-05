# coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField("博客题目",max_length=100)		
    category = models.CharField("博客标签",max_length=50,blank=True)
	#DateField.auto_now_add,当对象首次被创建时，自动将该字段的值设置为当前时间，\
	#通常用于表示对象创建时间。auto_now则自动添加修改日期
    date_time = models.DateField("博客日期",auto_now_add=True)
    modify_time = models.DateField("修改日期",auto_now=True)
    content = models.TextField("博客文章正文",blank=True,null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']   #按照时间下降排序
        db_table = "blogitem"       #表格名称

