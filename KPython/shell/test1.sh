#!/bin/bash
#test +测试语句  -gt
if test 3 -gt 2   #为真执行  3>2
then
  echo "3 -gt 2"
fi


if [ 3 -gt 2 ]
then
echo "3 -gt 2"
fi

if [ $1 -gt 0 -a $1 -le 10 ]
# # [ $1 -gt 0] && [ $1 -le 10 ]  ||   #bash test1.sh 3
then
echo "0 <$1 <= 10"
fi

if [ $1 = "hello" ]
then
echo "hello"
fi

if [ -e file ]
then
echo "文件存在"
fi

if test -n "hello"
then
echo "hello"
fi
