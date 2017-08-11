# shell 数组
#！/bin/bash

array=(1 2 3 4 5)
array=(abc 2 3 4 5)
echo ${array[2]}
echo ${array[@]}
echo ${array[*]}
echo ${#array[*]}
echo ${#array[1]}
echo ${array[*]:3}
echo ${array[*]:1:4}
