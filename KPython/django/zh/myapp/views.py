# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response

from django.http import HttpResponse,Http404
from django.template import loader
import time
from myapp.models import *
from django.db.models import F,Q
import datetime
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
# from FIL import Image
#全局
def kang(request):
    NAME='kang'
    TEL='18755667777'
    return locals()

# Create your views here.
def fun():
    return "hello"

class A(object):
    a="class->a"
    def f(self):
        return "jest a A:fun"

def first(request):
    return HttpResponse("增辉")

def b(request):
    t=loader.get_template('b.html')
    html=t.render({})
    return HttpResponse(html)

def w(request):
    # return render_to_response('b.html',{})
    #全局定量
    return render(request,'b.html',{})

def temp(request):
    # k=time.localtime()
    datetime = time.localtime()
    # return render(request,'1.html',{'datetime':k})
          #收集函数所有局部变量形成字典输出
    return render(request,'1.html',locals())

def display_meta(request):
    num=1
    s="hello"
    l=[1,2,'c','nihao']
    t=(4,5,'d','tuple')
    d={'a':'one','b':'two','c':'three'}
    f=fun()
    obj=A()

    return render(request,'meta.html',\
    {'num':num,'s':'s','list':l,'tuple':t,'dict':d,'fun':f,'obj':obj})

def tag(request):
    error="error"
    l=['一','鸣','惊','人']
    return render(request,'tags.html',{'error':error,'list':l})

def fil(request):
    num=1
    k="HELLO "

    return render(request,'f.html',{'num':num,'k':k})

def base(request):
    return render(request,'extend.html',{})

def nav(request):
    return render(request,'nav.html',{})

def load(request):
    return render(request,'static.html',{})

def mydb(request):
# # #增
    # Author.objects.create(first_name = 'Jame',last_name = 'Green',email= 'jm@123.com')

    Publisher.objects.create(name ="women",address = "beijing",city = "beijing",state_province = "haidian",country = "china",website = 'http://192.168.0.1')
    Book.objects.create(title = "shoubiao",publication_date=datetime.datetime.now(),Publisher_id = 1)
    Book.objects.create(title = "huahua",publication_date=datetime.datetime.now(),Publisher_id = 2)
    Book.objects.create(title = "shijie",publication_date=datetime.datetime.now(),Publisher_id = 1)

#     # obj = Author(first_name = 'kang',last_name = 'chuanshuo',email= 'yun@123.com')
#     # obj.save()

    # dic = {'first_name': 'kang','last_name' : 'chuanshuo','email':'hm@123.com'}
    # obj = Author(**dic)
    # obj.save()
#删
    # Publisher.objects.filter(id__gt=3).delete()
# #改
    # Author.objects.filter(id=1).update(id = '2',first_name = 'lili')
    # Author.objects.filter(id=4).update(id = '1')
    # obj = Author.objects.get(id = 2)
    # obj.last_name = "huazi"
    # obj.save()

#查看 select * from Author
    # a = Author.objects.all()  #每条记录的生成的对象
    # b = Author.objects.all().values('email') #取出所有记录指定字段
    # c = Author.objects.all().values_list('first_name','email') #取出所有记录指定字段
    # # # d = Author.objects.get(id = 1) #获取某一条记录的对象
    # e = Author.objects.filter(id = 1)  #获取某一记录的对象


    # Author.objects.filter().update(age = F('age') + 1)

    # q = Q()
    # print dir(q)
    #
    # q.connector = 'AND'
    # q.children.append(('id',2))
    # q.children.append(('last_name','Green'))
    #
    # f = Author.objects.filter(q)
    #
    # return HttpResponse(f[0].first_name)



    return HttpResponse("ok")
    # return HttpResponse(c)
    # return HttpResponse(d.email)
    # return HttpResponse(a.count())
    # return HttpResponse(e[0].email)



#添加书的关系
def mtm(request):
    # book1 = Book.objects.get(id = 1)
    # s = book1.publisher.name
    # ii = book1.author.all()
    #
    # pub1 = Publisher.objects.get(id = 1)
    #     # 外调关系需要加上_set
    # kang = pub1.book_set.all()
    #
    # author1 = Author.objects.get(id = 1)
    # nm = author1.book_set.all()

    # author_list = book1.author.all()

    # count = Book.objects.title_count('huahua')
    # count = Book.myobjects.title_count('huahua')
    book2_list = Book.myobjects.all().little()



    return HttpResponse(book2_list)

def page(request,article_list,n):
    paginator = Paginator(article_list,n)
    try:
        p = int(request.GET.get('page',1))
        article_list = paginator.page(p)
    except (EmptyPage,InvalidPage,PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list

def getPage(request):
    article_list = ['a1','a2','a3','a4','a5','a6','a7']
    article_list = page(request,article_list,5)
    return render(request,'page.html',{'article_list':article_list})

def postImage(request):
    return render(request,'image.html',{})

def message(request):
    try:
        img = Ad(title = 'imgTest',img = request.FILES.get('picfile'))
        img.save()
    except Exception,e:
        return HttpResponse("Error:%s"%e)
    return HttpResponse("post images")
    
# def postImage(request):
#     return render(request,'image.html',{})
#
# def message(request):
#     try:
#         imgFile = request.FILES['picfile']
#         img = Image.open(imgFile)
#         img.save("/home/linux/成功需要改变,改变就在一瞬间/Kpython/django/zh/media/a.png",'png')
#     except Exception,e:
#         return HttpResponse("Error:%s"%e)
#     return HttpResponse("post images")
