#!/bin/bash
if [ $# -ne 1 ]
then
  exit 1
fi

if ! [ -e $1 ]
then
echo "the $1 not exist"
exit 1
fi

if [ -f $1 ]
then
  echo "$1 是一个普通文件"
elif [ -d $1 ]
then
echo "$1 is a directory"
else
  echo "$1 其他类型文件"
fi
