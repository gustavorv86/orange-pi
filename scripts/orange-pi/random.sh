#!/bin/bash

LEN=32

if [[ $# -ge 1 ]]; then
	LEN=$1
fi

cat /dev/urandom | tr -dc 'a-km-zA-NP-Z0-9' | fold -w $LEN | head -n 1
