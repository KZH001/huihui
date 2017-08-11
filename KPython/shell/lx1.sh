#!bin/bash
cd $HOME
path="dir/if_file"
if [ -e dir ]
then
  rm dir -rf
fi
mkdir dir
touch $path
if ! [ -e $path ]
then
echo "creat file failed"
exit 1
else
  if [ -r $path ]
  then
    echo -n "r"
  else
    echo -n "-"
  fi
  if [ -w $path ]
  then
    echo -n "w"
  else
    echo -n "-"
  fi
  if [ -x $path ]
  then
    echo  "x"
  else
    echo "-"
  fi
fi
