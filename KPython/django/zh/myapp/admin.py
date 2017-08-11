# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from myapp.models import *

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    search_fields = ('first_name','last_name')
                        #  模型管理
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','city','address')
    search_fields = ('name','city')


class BookAdmin(admin.ModelAdmin):
    list_display = ('publication_date','title')

                    #出版日期  标题
    search_fields = ('title',)
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title','author','publisher','publication_date')
# 管理
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Ad)
