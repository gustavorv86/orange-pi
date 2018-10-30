#!/bin/bash
#

cd 433Utils
git pull
cd -

cd python/derekstavis/python-sysfs-gpio
git pull
cd -

cd python/duxingkei33/orangepi_PC_gpio_pyH3
git pull
cd -

cd python/kylemanna/pydevmem
git pull
cd -

cd python/vitiral/gpio
git pull
cd -

cd python/vsergeev/python-periphery
git checkout -- .
git pull
cd -

cd WiringOP/flexiti-h3/WiringOP
git pull
cd -

cd WiringOP/loboris-h3/WiringOP
git pull
cd -

cd WiringOP/kazukioishi-h5/WiringOP
git pull
cd -

cd WiringOP/xpertsavenue-zero/WiringOP-Zero
git pull
cd -

cd WiringOP/OrangePiLibra-RDA8810/WiringPi
git pull
cd -

cd WiringOP/zhaolei-h3/WiringOP
git pull
cd -
