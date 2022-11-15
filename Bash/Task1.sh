#!/usr/bin/env bash

year=$(date +%Y)
home="/home/hawila"
mon=$(date +%m)
day=$(date +%d)
hour=$(date +%I)
pm_or_am=$(date +%p)

create_year_dir(){
	mkdir $home/Reports/$year
	for i in {1..12};
	do
		mkdir $home/Reports/$year/$i
	done
}
create_file(){
	if [ ! -e $home/Reprots/$year/$mon/$day.xls ]; then
		echo >> $home/Reports/$year/$mon/$day.xls
	fi
}

if [ -d ~/Reports ];
then
	if [ ! -d ~/Reports/$year ];
	then
		create_year_dir
		create_file
	else
		create_file
	fi
else
	mkdir $home/Reports
	mkdir $home/Backups
	create_year_dir
	create_file
fi

#backup only between 12Am : 5 AM

if [ $hour -lt 5 ] || [ $hour -eq 12 ] && [ "$pm_or_am" == "AM" ];then
	if [ ! -e $home/Backups/"$year-$mon-$day.xls" ];then
		echo >> $home/Backups/"$year-$mon-$day.xls"
	fi
fi
