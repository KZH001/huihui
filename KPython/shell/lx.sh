# #!/bin/bash
# read a
# read b
# read c
# read d
#
# kk=`expr $a \* $b + $c - $d / $b`
#
# echo $kk

#!/bin/bash
#  read a b c d
read a
read b
read c
read d

 result=`expr $a \* \( $b + $c \) - $d / $b`
 echo "result = $result"
