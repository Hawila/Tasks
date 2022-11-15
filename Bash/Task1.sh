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
	echo "Reports Exists Checking Year"
	if [ ! -d ~/Reports/$year ];
	then
		echo "Creating $year Dir"
		create_year_dir
		create_file
		echo "File $day.xls Created in $home/Reports/$year/$mon"
	else
		echo "Creating File $day.xls"
		create_file
		echo "File $day.xls Created in $home/Reports/$year/$mon"
	fi
else
	echo "making Reports dir ..."
	mkdir $home/Reports
	echo "making Backups dir ..."
	mkdir $home/Backups
	create_year_dir
	create_file
	echo "File $day.xls Created in $home/Reports/$year/$mon"
fi

#backup only between 12Am : 5 AM
echo "Checking Time .."

echo "$hour $pm_or_am"

if [ $hour -lt 5 ] || [ $hour -eq 12 ] && [ "$pm_or_am" == "AM" ];then
	echo "File $day.xls Backedup as  $home/Backups/"$year-$mon-$day.xls""
	cp  $home/Reports/$year/$mon/$day.xls $home/Backups/"$year-$mon-$day.xls"
else
	echo "Backup Failed"
fi

