#coding=utf-8
from django import template
register = template.Library()
#装饰器
@register.filter(name = 'rep')
def rep(value,arg):
    return value.replace(arg,'$')
