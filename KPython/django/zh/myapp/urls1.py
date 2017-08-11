#coding=utf-8

from django.conf.urls import url
from myapp.views import *

urlpatterns = [
    url(r'^first/$',first),
    url(r'^b/$',b),
    url(r'^w/$',w),
    url(r'^kzh/$',temp),
    url(r'^kk/$',display_meta),
    url(r'^tags/$',tag),
    url(r'^f/$',fil),
    url(r'^base/$',base,name='base'),
    url(r'^include/$',nav),
    url(r'^static/$',load),
]
urlpatterns += [
    url(r'^models/$',mydb),
    url(r'^models1/$',mtm),
]
urlpatterns += [
    url(r'^page/$',getPage),
    url(r'^postImage/$',postImage),
    url(r'^message/$',message),
]
