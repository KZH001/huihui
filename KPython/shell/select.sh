#!/bin/bash
echo "what is your favorite color?"
select color in  "red" "blue"
do
  echo "You have selected $color"
  break
done
