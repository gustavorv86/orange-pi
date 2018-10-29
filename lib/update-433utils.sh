#!/bin/bash
#

if [ ! -d 433Utils ]; then
	git clone --recursive git://github.com/ninjablocks/433Utils.git
fi
cd 433Utils
git checkout -- .
git pull
