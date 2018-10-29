#!/bin/bash
#

mkdir -p WiringOP
cd WiringOP

mkdir -p zhaolei-h3
cd zhaolei-h3
if [[ ! -d WiringOP ]]; then
	git clone https://github.com/zhaolei/WiringOP.git -b h3
fi
cd WiringOP
git checkout -- .
git pull
cd ..
cd ..

mkdir -p flexiti-h3
cd flexiti-h3
if [[ ! -d WiringOP ]]; then
	git clone https://github.com/flexiti/WiringOP.git -b h3
fi
cd WiringOP
git checkout -- .
git pull
cd ..
cd ..

mkdir -p loboris-h3
cd loboris-h3
if [[ ! -d WiringOP ]]; then
	git clone https://github.com/loboris/WiringOP.git -b h3
fi
cd WiringOP
git checkout -- .
git pull
cd ..
cd ..

mkdir -p kazukioishi-h5
cd kazukioishi-h5
if [[ ! -d WiringOP ]]; then
	git clone https://github.com/kazukioishi/WiringOP.git -b h5
fi
cd WiringOP
git checkout -- .
git pull
cd ..
cd ..

mkdir -p xpertsavenue-zero
cd xpertsavenue-zero
if [[ ! -d WiringOP-Zero ]]; then
	git clone https://github.com/xpertsavenue/WiringOP-Zero.git
fi
cd WiringOP-Zero
git checkout -- .
git pull
cd ..
cd ..

mkdir -p OrangePiLibra-RDA8810
cd OrangePiLibra-RDA8810
if [[ ! -d WiringPi ]]; then
	env GIT_SSL_NO_VERIFY=true git clone https://github.com/OrangePiLibra/WiringPi.git
fi
cd WiringPi
git checkout -- .
git pull
cd ..
cd ..

echo "Done"
echo
