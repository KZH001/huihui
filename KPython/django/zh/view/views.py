# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.views import View



# Create your views here.

class MyView(View):
    def get(self,request):
        return HttpResponse('<h2>万马奔腾</h2>')

def test(request,offset):
    return HttpResponse(offset)

def foo_bar(request,template_name):
    print "最吉祥"
    return render(request,template_name,{})
