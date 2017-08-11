# # #!/usr/bin/python
# # #coding=utf-8
# # # 创建进程
# ##调用模块
# # import os
# # 时间
# # from time import sleep
# # 返回值=模块.函数
# # pid = os.fork()
# # 执行完之后生成两个模块
# # if pid < 0:
# #     print "create process faile"
# # elif pid == 0:
# #     # print pid
# #     # print "This is a child process:",os.getpid()
# #     print "This is a child process:"
# #
# # else:
# #     #睡眠时间
# #     # sleep(0.1)
# #     # print pid
# #     # print "This is a parent process",os.getpid()
# #     print "This is a parent process"
# #
# # print "+++++++++"
#
import os
from time import sleep
pid = os.fork()

if pid < 0:
    print "create process faile"
elif pid == 0:
    # 进程优先级，睡眠时间
    sleep(0.1)
    # 输出id
    print "This is a child process:",os.getpid()

else:
    # 处理子进程(僵尸进程)
    os.wait()
    print "This is a parent process",os.getpid()
    # 无限循环
    while True:
        pass
        # print "+++++++"

print "++++++++++++"
