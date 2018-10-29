SHELL=/bin/bash

TARGET=control-button
BUILD=build
CFLAGS=-Wall -Wextra -ggdb
LDFLAGS=-lwiringPi

all: make_dirs ${TARGET}

make_dirs:
	@mkdir -p build

${BUILD}/control-button.o: control-button.c
	gcc ${CFLAGS} -c control-button.c -o ${BUILD}/control-button.o

${TARGET}: ${BUILD}/control-button.o
	gcc ${CFLAGS} ${BUILD}/control-button.o -o ${TARGET} ${LDFLAGS}
