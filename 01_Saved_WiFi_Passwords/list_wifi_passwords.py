#
#  This script lists all the saved WiFi Passwords in the system.
#  This script works with :
#   -> Windows
#  
#  Copyright (C) 2020-2021, Manjot Sidhu <manjot.techie@gmail.com>
#                           PitchBlack Recovery Project <pitchblackrecovery@gmail.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  NOTE: This script is only meant for informational and educational purposes only.
# 

import os
import subprocess
import re
from sys import platform


def is_windows():
	if platform == "linux" or platform == "linux2":
	    return False
	elif platform == "win32":
	    return True


def exec_cmd(cmd):
	#print(f'Executing Command -> {cmd}')
	p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, shell=True)
 
	(output, err) = p.communicate()
	 
	p_status = p.wait()
	return (output.decode("utf-8"), p_status)


def get_profiles_win():
	get_profiles_cmd = exec_cmd("netsh wlan show profile")
	result = re.findall('All User Profile[\s\t]+:\s(\w+)', get_profiles_cmd[0])
	return result


def get_pass_win(profile):
	pass_cmd = exec_cmd(f'netsh wlan show profile {profile} key=clear')
	result = re.search('Key Content[\s\t]+:\s([^\n\t]+)', pass_cmd[0])

	if result is None:
		return None
	else:
		return result.group(1)


def get_passwords_win():
	print(f'{"SSID".ljust(20)}: Password')
	print("-"*30)
	for profile in get_profiles_win():
		pwd = get_pass_win(profile)
		print(f'{profile.ljust(20)}: {pwd}')


def get_passwords_linux():
	print("TODO")


def main():
	if is_windows():
		get_passwords_win()
	else:
		get_passwords_linux()

main()