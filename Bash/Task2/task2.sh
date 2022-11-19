#!/usr/bin/env bash

source ./Lib.sh

#bonus
SECONDS=0
while [ ! -e $HOME/sprint.bash ];do
	t_elapsed=$SECONDS
	echo "while loop ran for $(($t_elapsed / 60)) minutes $(($t_elapsed % 60)) seconds before file exist" > $HOME/while.txt
done
echo "File exist"
cat $HOME/while.txt
