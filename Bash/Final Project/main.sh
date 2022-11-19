#!/usr/bin/env bash
source ./ssh_Bconfig.sh
source ./lib.sh



#foreverloop to keep printing menu till exit command is given
while true;do
	#root priv check
	gr=$(groups $USER)
	if grep -q 'wheel' <<< "$gr" || [ "$EUID" -eq 0 ] || [ "$(whoami)" == root ] || grep "$USER" "/etc/sudoers";
	then
        show_menu $1 $2 $3
		read s
		case "$s" in
			1) change_ssh_port "$1";;
			2) disable_root_login;;
			3) fwall_selin "$1";;
			4) audit_group;;
			5) user_add "$2" "$3";;
			6) reports_create;;
			7) supdate;;
			8) epel;;
			9) fail2ban;;
			10) report_backup;;
            11) manager_add;;
            12) sync;;
			[^q]) echo "invalid input PLease choose Correct option (q to quit)";;
			q) exit
		esac
	else
   	echo "only root user or sudoer user can run the script"
	exit 1
	fi
done
