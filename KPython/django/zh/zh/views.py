#coding=utf-8
from django.http import HttpResponse
from django.template import loader

import datetime

def kang(request):
    return HttpResponse("康增辉")

def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body>It is now %s.<body><html>"%now
    return HttpResponse(html)

def b(request):
    t=loader.get_template('b.html')
    html=t.render({'time':datetime.datetime.now()})
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()

    kk = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html="<html><body> In %s hours,it will be %s.<body><html>"%(offset,kk)
    return HttpResponse(html)

def baidu(request,offset):
    if offset =="kang":
        return HttpResponse("康")
    elif offset == "zenghui":
        return HttpResponse("增辉")
    else:
        raise Http404()
