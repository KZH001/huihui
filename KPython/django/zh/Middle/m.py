# coding=utf-8
# 中间件配置   类的组合
from django.utils.deprecation import MiddlewareMixin

class Row1(MiddlewareMixin):
    def process_request(self,request):
        print "成功需要改变"

    def process_response(self,request,response):
        print "来改变"
        return response


class Row2(MiddlewareMixin):
    def process_request(self,request):
        print "改变就在一瞬间"

    def process_response(self,request,response):
        print "链接"
        return response
