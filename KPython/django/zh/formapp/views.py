# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from formapp.forms import RemarkForm,BookForm
# from formapp.forms import RemarkForm,AuthorForm
from myapp.models import Book
# from myapp.models import Author

# Create your views here.
def search_form(request):
    return render(request,'search_form.html',{})

def search(request):
    print request.method
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        return HttpResponse("I have get the '%s'"%q)
    else:
        return render(request,'search_form.html',{'error':True})

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject')

        if not request.POST.get('email',''):
            errors.append('Enter a email address')

        if not request.POST.get('message',''):
            errors.append('Enter a message')

        if not errors:
            #return HttpResponseRedirect("/form/contact/thanks")
            return redirect("/form/contact/thanks")

    return render(request,"contact_form.html",{'errors':errors,'subject':request.POST.get('subject'),'email':request.POST.get('email'),'message':request.POST.get('message')})

def thanks(request):
    print "come on"
    #return HttpResponse("Thanks,we have get your message")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def formtest(request):
    if request.method == 'POST':
        form = RemarkForm(request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            print cd['subject']
            print cd['mail']
            print cd['topic']
            print cd['message']
            print cd['cc_myself']
            return HttpResponseRedirect('/form/form')
    else:
        form = RemarkForm()

    return render(request,'formset.html',{'form':form})


def bookset(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            dic = {'title':cd['title'],'publication_date':cd['publication_date'],'publisher_id':1}
            Author.objects.create(**dic)
            return HttpResponseRedirect('/form/bookform')
    else:
        form = BookForm()

    return render(request,'bookset.html',{'form':form})


# def bookset(request):
#     if request.method == 'POST':
#         form = AuthorForm(request.POST)
#         if form.is_valid():
#             cd  = form.cleaned_data
#             dic = {'first_name':cd['first_name'],'last_name':cd['last_name'],'age':cd['age'],'email':cd['email']}
#             Author.objects.create(**dic)
#             return HttpResponseRedirect('/form/bookform')
#     else:
#         form = AuthorForm()
#
#     return render(request,'bookset.html',{'form':form})

user_info = {
    'tai':{'pwd':'taiyang'},
    'yue':{'pwd':'yueliang'},
}
@csrf_exempt
def login(request):
    if request.method =='GET':
        return render(request,"login.html")
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        dic = user_info.get(u)
        if not dic:
            return render(requesty,'login.html')
        if dic['pwd'] == p:
            res = redirect("/from/index")
            res.set_cookie("user",u,max_age = 60,path = '/')
            return res
        else:
            return renser(request,'login.html')

def index(request):
    v = request.COOKIES.get('user')
    if not v:
        return redirect('/form/login')
    return render(request,'index.html',{'current_user':v})
