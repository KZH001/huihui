#coding=utf-8

from django.conf.urls import url
from view.views import *               #模板视图
from django.views.generic import TemplateView
                                     #重定向视图
from django.views.generic.base import RedirectView


urlpatterns = [       #特定名字和view调用名字一样    一种传参方式
    url(r'^test/(?P<offset>\d{1,2})/$',test),
    url(r'^foo/$',foo_bar,{'template_name':"foo.html"}),
    url(r'^bar/$',foo_bar,{'template_name':"bar.html"}),
]

urlpatterns += [
    url(r'^about/$',TemplateView.as_view(template_name = 'about.html')),
    url(r'^go-to',RedirectView.as_view(url='http://www.baidu.com')),
    url(r'^my_view',MyView.as_view()),
]
