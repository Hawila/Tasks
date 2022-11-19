#!/usr/bin/env bash
check_root_priv(){
	groups_of_user=$(groups $USER)
	if grep -q 'wheel' <<< "$groups_of_user" || [ $EUID -eq 0 ] || grep "$USER" "/etc/sudoers";
	then
       		echo "user have root privilages"
	else
		echo "user dont have root privilages"
	fi       
}

change_ssh_port(){
	echo "Enter new ssh Port to change"
	read port
	sed -i "s/#Port 22/Port $port/g" /etc/ssh/sshd_config
	echo "ssh Port Changed to $port"
}

disable_root_login(){
	echo -e "Modifying Deafult ssh Configuration...\ "
	sed -i "s/PermitRootLogin yes/PermitRootLogin no/g" /etc/ssh/sshd_config
	echo -e "Remote Login using root credintioal will be denied...\  "
}

add_user(){
	echo "Enter user you want to add"
	read user
	user_exist=$(grep "^$user" /etc/passwd)
	if grep -q "$user" <<< "$user_exist";then
		echo "$user exist"
	else
		echo "Add user to sudoers[y/n]"
		read ans
		if [ "$ans" == "y" ] || [ $ans == "yes" ];
		then
			useradd $user
			echo "$user ALL=(ALL) ALL" >> /etc/sudoers
		else
			useradd $user
		fi
	fi
}

home_backup(){
	echo "00 12 1 * * tar -czf /etc/home.tar.gz $HOME" > "$HOME/backup.txt"
	crontab "$HOME/backup.txt"
}