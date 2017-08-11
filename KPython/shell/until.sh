#!/bin/bash
k=10
until [ $k -lt 5 ]
do
  let "j=k*k"
  echo "$j = $k *$k"
  ((k--))
done
