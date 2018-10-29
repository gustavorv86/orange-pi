#!/bin/bash
#

apt-get update && apt-get -y dist-upgrade

#### SYSTEM ####
apt-get -y install \
cpufrequtils \
openssh-server \
wakeonlan \
wget \
xterm \
xauth \
gpiod \
evtest \
hwinfo \
lshw

#### DEVEL ####
apt-get -y install \
gcc \
gdb \
cgdb \
make \
libc6-dev \
git \
geany \
vim \
python3-dev \
python3-pip \
