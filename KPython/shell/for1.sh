# !/bin/bash
sum=0
for i in {1..100..2}  #每2取1
do
let "sum+=$i"
done
echo "sum = $sum"

kk=0
for (( i = 1; i <= 100; i++ ));
do
  kk=`expr $kk + $i`
done
echo "kk = $kk"
