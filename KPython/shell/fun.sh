# !/bin/bash
kk(){
  echo "k"
}
kk
echo "hanshu:`kk`"

kk(){
  echo "k"
  echo "z"
  }
  value=`kk`
  echo "hanshu:$value"

kk(){
  echo "k"
  echo "z"
  return 2
}
kk
echo $?

kk(){
  sum=0
  for i in {1..100}
  do
  let "sum+=$i"
  done
  echo "sum = $sum"
}
kk

kk(){
  sum=`expr $1 + $2`
  echo $sum
}
kk 1 2


count()
{
  if [ $# -ne 3 ]
  then echo "number of argument is not 3"
fi

s=0
case $2 in
  +)
  let "s = $1 + $3"
  echo "$1 + $3 = $s"
  ;;
  -)
  let "s = $1 - $3"
  echo "$1 - $3 = $s"
  ;;
  \*)
  let "s = $1 * $3"
  echo "$1 + $3 = $s"
  ;;
  \/)
  let "s = $1 / $3"
  echo "$1 / $3 = $s"
  ;;
  *)
  echo "you iput is wrong!"
esac
}
echo "type your word(e.g. 1+1)"
read a b c
echo $b
count $a $b $c


kk()
{
  i=1
  sum=0
  while [ $i -le $1 ]
  do
  n=`expr $i % 2`
  if [ $n -ne 0 ]
  then
  let "sum+=i"
fi
  ((i++))
  done
  echo "sum = $sum"
}
kk $1
