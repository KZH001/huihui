#!/bin/bash
if [ $# -ne 1 ]
then
exit 1
fi

for file in `ls`
do
  if [ $1 = $file ]
  then
    echo "find $1"
    exit 0
  fi
done
echo "not find $1"
