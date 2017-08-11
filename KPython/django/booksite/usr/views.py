# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
#from django.template import RequestContext
from forms import *
from usr.models import *
from django.contrib.auth.hashers import make_password
from django.contrib import auth
                          #修饰符                   要求        许可
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
    # 许可
@permission_required('add_User',login_url = '/login/')
def thanks(request):                        # 注册
    return HttpResponse("Thanks for your register")

#@permission_required(login_url = '/thanks/')
def reg(request):
    try:
        if request.method == 'POST':
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                cd = reg_form.cleaned_data                                                                                  #移动
                User.objects.create(username=cd['username'],password=make_password(cd['password']),email=cd['email'],mobile=cd['tel'])

                return HttpResponseRedirect("/login/")
            else:
                return render(request,'failure.html',{'reason':reg_form.errors})
        else:
            reg_form = RegForm()
    except Exception as e:
        print e
    return render(request,'reg.html',locals())

            #要求
@login_required(login_url = '/login/')
def login_test(request):
    return HttpResponse('Thank you for login')

def login(request):
    errors=[]
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if not request.POST.get('username',''):
            errors.append('Enter a username.')
        if not request.POST.get('password',''):
            errors.append('Enter a password.')
        if not errors:                   #通过身份验证
            if not request.user.is_authenticated():
                user = auth.authenticate(username=username,password=password)
                if user is not None and user.is_active:
                    auth.login(request,user)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
                else:
                    return HttpResponse('usrname or password invalid.')
            else:                                 #已经
                return HttpResponse("You have already login")
    return render(request,'user_login.html',{'errors':errors,})

def loginout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")
