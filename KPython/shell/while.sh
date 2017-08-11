#!/bin/bash
# sun=0
# i=1
#
# while [ $i -le 100 ]
# do
#   let "sum+=i"
#   ((i++))
# done
# echo "sum = $sum"


sum=0
k=1
while [ $k -le 3 ]
do
  let "sum+=k"
  ((k++))
done
echo "sum = $sum"
