# #!/usr/bin/python
#coding=utf-8
# def printlove(start,length,midnumber=0,flag=31):
#     for i in range(31):
#         if i<start or i>start+length-1 and i<15-(midnumber-1)/2 or i>15+(midnumber-1)/2 and i<31-start-length or i> 30-start or i==flag:
#             print " ",
#         else:
#             print "*",
#     print ""
# for i in range(16):
#     if i ==0:
#             printlove(4,3)
#     elif i==1:
#             printlove(1,9)
#     elif i>=2 and i<=5:
#             printlove(0,i+10)
#     elif i==6:
#             printlove(1,7,7,15)
#     elif i>=7 and i<=8:
#             printlove(i-5,6,5-(i-7)*2)
#     elif i==9:
#             printlove(5,6,1)
#     elif i==10:
#             printlove(8,6,1)
#     elif i==15:
#             printlove(15,1,1)
#     else:
#             printlove(i-1,16-i,1)

# import copy
# aa=[]
# bb=[]
# def Fibonacci(aa,n):
#     bb.append(0)
#     if n ==1:
#         return [1]
#     for i in range(n):
#         if i==0 or i==n-1:
#             bb[i]=1
#         else:
#             bb[i]=aa[i-1]+aa[i]
#     return bb
# cc=68
# for i in range(17):
#     cc=cc-4
#     aa=copy.deepcopy(Fibonacci(aa,i+1))
#     for i in range(cc/2):
#         print " ",
#     for i in aa:
#         print str(i).ljust(6),
#     print " "
