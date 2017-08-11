# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#方法                      查询集
class BookQuerySet(models.QuerySet):
    def little(self):
        return self.filter(id__lt = 3)

        # 继承          #类
class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model,using=self._db)

    def title_count(self,keyword):
        return self.filter(title__icontains = keyword).count()
#
class Publisher(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 60)
    state_province = models.CharField(max_length = 30)
    country = models.CharField(max_length = 50)
    website = models.URLField(verbose_name = "网址")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'publisher'
        ordering = ['name']
        verbose_name = "出版社"
        verbose_name_plural = verbose_name


class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    age = models.IntegerField(null = True,default = 10)
    email = models.EmailField(blank = True )

    def __unicode__(self):
        return "%s %s"%(self.first_name,self.last_name)

    class Meta:
        db_table = 'author'
        verbose_name = "作者"
        verbose_name_plural = verbose_name



class Book(models.Model):
    title = models.CharField(max_length = 100)
    publication_date = models.DateField(blank = True,null = True)
    #    作者在书里面建立关系 多对多
    author = models.ManyToManyField(Author)
    #  出版社在书里面建立关系 一对多
    publisher = models.ForeignKey(Publisher)

    objects = BookManager()
    objects = models.Manager()
    #
    myobjects = BookManager()

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'book'
        verbose_name = "书"
        verbose_name_plural = verbose_name
        ordering = ['title']

class Ad(models.Model):
    title = modls.CharField(max_length = 100)
    img = models.ImageField(upload_to = "avatar/%Y%m%",default = 'a.png',verbose_name='用户头像')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
