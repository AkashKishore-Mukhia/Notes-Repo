#!/bin/bash

# Author: Akash Mukhia

# Description
# Script will create a backup of the current working directory

#Usage
# bash <script-name>

echo backup in-progress...
tar -cvf ~/Documents/Notes-Repo/Bash/my_backup_"$(date +%d-%m-%Y_%H-%M-%S)".tar ~/Documents/Notes-Repo/Bash* 2>/dev/null
exit 0