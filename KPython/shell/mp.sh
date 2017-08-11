!/bin/bash

read -a k
for((i=0;i<${#k[@]};i++))
{
   for((j=0;j<${#k[@]}-1;j++))
   {
     if [[ ${k[j]} -gt ${k[j+1]} ]];
     then
        n=${k[j]}
          k[j]=${k[j+1]}
          k[j+1]=$n
      fi
}
}
echo ${k[@]}



array=(56 42 15 36 78 95 42 12 5)
echo ${array[@]}
echo "++++++++"
i=0
length=${#array[@]}
echo "length = $length"
while [[ $i -lt `expr $length - 1` ]]
do
  num=`expr $length - $i - 1`
  for ((j = 0; j < num ; j++))
  do
    if [[ ${array[$j]} -gt ${array[$j + 1]} ]]
    then
      tmp=${array[$j]}
      array[$j]=${array[$j + 1]}
      array[$j +1]=$tmp
    fi
  done
  let "i+=1"
done
echo ${array[@]}
