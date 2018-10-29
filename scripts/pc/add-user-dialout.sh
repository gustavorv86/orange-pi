#!/bin/bash

USE_SUDO='true'

username=${USER}

if [[ ${username} == 'root' ]]; then
	echo 'ERROR: run as normal user'
	exit 1
fi

if [[ ${USE_SUDO} == 'true' ]]; then
	sudo usermod -a -G dialout ${username}
else
	su -c "usermod -a -G contabilidad ${username}"
fi

echo 'Done'

