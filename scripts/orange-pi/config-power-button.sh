#!/bin/bash
#

CFGFILE=/etc/acpi/events/button_power

apt-get -y install acpid

echo "event=button/power" >> ${CFGFILE}
echo "action=/sbin/shutdown -h now" >> ${CFGFILE}

chmod +x ${CFGFILE}

service acpid restart

