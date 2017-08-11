#!/bin/bash
read a b
let "c = a * b"
echo $c
let "c*=5"  # c = c * 5
echo $c
let "c++"    # a++  ===>  a=a+1
((c++))
((c+=10))
echo $c

`echo "1.1 + 2.2" | bc`
echo $value
