# #1/usr/bin/python
# #coding=utf-8

# 斐波那契数列的函数
# def fib(n):
#     a,b=0,1
#     while a<n:
#         print (a, end = ' ')
#         a,b=b,a+b
#     print()
# fib(100)

#水仙花数
# for i in range(1,1000):
#     sum=0 #各个位数的立方和
#     k=i
#     while k:
#         sum=sum+(k%10)**3   #累加
#         k//=10   #地板除
#     if sum==i:
#         print(i)

# 1000以内完数
# for i in range(1, 1000):
#     sum = 0
#     for k in range(1, i):
#         if i % k == 0:
#             sum = sum + k
#     if i == sum:
#         print(i)

#100以内质数
# import math
# def k(n):
#   return filter(lambda x:not [x%i for i in range(2,int(math.sqrt(x))+1) if x%i ==0],range(2,n+1))
# print k(100)

# 9 * 9
# for i in range(1, 10):
#   print
#   for j in range(1, i+1):
#     print "%d*%d=%d" % (i, j, i*j),

# #最大值及位置
# k=[[2,1,3,4],[4,6,7,5],[3,4,6,1]]
# # k=[[5,2,7,3],[4,9,2,8],[5,1,6,7]]
# # a=len(k)
# # b=len(k[0])
# # for i in k:
# #     for j in i:
# #         print j,
# #     print ""
# # i=j=0
# # x=y=0
# # max=k[0][0]
# # while i < a:
# #     j=0
# #     while j <b:
# #         if k[i][j]>max:
# #             max=k[i][j]
# #             x,y=i,j
# #         j += 1
# #     i+=1
# #     print "k[%d][%d]=%d"%(x,y,max)
# # #鞍点
# # for i in k:
# #     m=max(i)
# #     n=i.index(m)
# #     j=0
# #     while j < len(k):
# #         if k[j][n]>m:
# #             break
# #         j+=1
# #     else:
# #         print i[n]
# #杨辉三角
k=[]

for i in range(10):
    k.append([])
    k[i].append(1)
    for j in range(1,i+1):
        k[i].append(k[i-1][j-1]+k[i-1][j])
    k[i].append(0)
for i in k:
    i.pop()
    print i
