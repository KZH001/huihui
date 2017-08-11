#！/usr/bin/python
#coding=utf-8
# 丑数定义余数为0,商为1
#创建函数
def Kang(self,N):
    # 条件定义
    k=[2,3,5]
    # 判断真假
    if N == 1:
        print True
    if N == 0:
        print False
        # 循环判断
    while True:
        # 判断语句
        if N/k == 1 or N%k == 0:
            print True
        else:
            print False
