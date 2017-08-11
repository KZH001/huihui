"""zh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from zh import views
from django.views.static import serve
from django.conf import settings
# from myapp.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.kang,name='kang'),
    url(r'^time/$',views.current_datetime),
    url(r'^b/$',views.b),
    url(r'^time/plus/(\d{1,2})/$',views.hours_ahead),
    url(r'^baidu1/$',views.baidu,{'offset':"kang"}),
    url(r'^media/(?P<path>.*)$'),serve,{'document_root':settings.MEDIA_ROOT}
]

urlpatterns += [
    url(r'^app/',include('myapp.urls1')),
    url(r'^form/',include('formapp.urls2')),
    url(r'^view/',include('view.urls')),
]
