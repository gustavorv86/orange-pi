#!/bin/bash
#

mkdir -p python
cd python

mkdir -p derekstavis
cd derekstavis
if [ ! -d python-sysfs-gpio ]; then
	git clone https://github.com/derekstavis/python-sysfs-gpio
fi
cd python-sysfs-gpio
git checkout -- .
git pull
cd ..
cd ..

mkdir -p duxingkei33
cd duxingkei33
if [ ! -d orangepi_PC_gpio_pyH3 ]; then
	git clone https://github.com/duxingkei33/orangepi_PC_gpio_pyH3.git
fi
cd orangepi_PC_gpio_pyH3
git checkout -- .
git pull
cd ..
cd ..

mkdir -p kylemanna
cd kylemanna
if [ ! -d pydevmem ]; then
	git clone https://github.com/kylemanna/pydevmem
fi
cd pydevmem
git checkout -- .
git pull
cd ..
cd ..

mkdir -p vitiral
cd vitiral
if [ ! -d gpio ]; then
	git clone https://github.com/vitiral/gpio
fi
cd gpio
git checkout -- .
git pull
cd ..
cd ..

mkdir -p vsergeev
cd vsergeev
if [ ! -d python-periphery ]; then
	git clone https://github.com/vsergeev/python-periphery
fi
cd python-periphery
git checkout -- .
git pull
cd ..
cd ..

