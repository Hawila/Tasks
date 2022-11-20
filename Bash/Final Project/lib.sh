#!/usr/bin/env bash

audit_group(){
    groupadd -g 20000 -f Audit
    echo "Group Audit added Successfuly"
}

user_add(){
    user_exist=$(grep "^$1" /etc/passwd)
	if grep -q "$1" <<< "$user_exist";then
		echo "$1 exist"
	else
        pass=$(perl -e 'print crypt($ARGV[0], "sprint")' $2)
        useradd -m -p "$pass" "$1" -g Audit 
		add_check=$(grep "^$1" /etc/passwd)
        if grep -q "$1" <<< "$add_check";then
		echo "$1 Added to the system"
        else
        echo "Failed to add user "
        fi
	fi
}
reports_create(){
    		mkdir -p $HOME/reports && touch $HOME/reports/2021-{1..12}-{1..31}.xls
    		echo "Reports successfully Created in $HOME/reports"
   		echo "Config Reports permissions..."
    		chmod 660 $HOME/reports/*
}

supdate(){
	echo "updating Centos  "
	yum -y "update"
}

epel(){
	echo "Enable EPEL Package "
	yum install "epel-release"
}
fail2ban(){
	echo "installing Fail2ban"
       	yum install "fail2ban"
	systemctl enable "fail2ban" 
       	systemctl start "fail2ban"	
}
report_backup(){
    mkdir -p $HOME/backups
	echo "00 1 * * 1-4 tar -czf $HOME/backups/reports-$(date +%U)-$(date +%w).tar.gz $HOME/reports" > "$HOME/rbackup.txt"
	crontab "$HOME/rbackup.txt"
}

manager_add(){
    useradd -u 30000 manager
    if [ $? -eq 0 ];then
	    echo "Manager has been added to the server"
    else
	    echo "faild to add manager to server"
    fi
}
sync(){
	s="$HOME/reports/*"
	d="/home/manager/audit/reports"
	mkdir -p /home/manager/audit
	mkdir -p /home/manager/audit/reports
	echo "00 2 * * 1-4 sync $s $d" > "/tmp/sync.txt";crontab "/tmp/sync.txt"
	echo "$USER crontab updated"
}

show_menu(){
    echo "PLease Choose An option(press q to exit)"
    echo "1- Change ssh port to $1"
    echo "2- Disable root Login"
    echo "3- config Firewall and SELINUX to allow port $1"
    echo "4- Add Audit Group"
    echo "5- Add user($2) and encrypt password($3)"
    echo "6- Create Reports"
    echo "7- System Update"
    echo "8- Enable EPEL Repo"
    echo "9- install fail2ban"
    echo "10- Backup Reports dir"
    echo "11- add manager to the system"
    echo "12- Syncronize Reports with manager"
}