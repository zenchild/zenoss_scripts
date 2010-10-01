#!/bin/bash

. ./0ENV.sh  # add connection variables in here

for zdev in `cat output.txt`
do
	curl -u ${ZUSER}:${ZPASS} "http://${ZSERVER}/zport/dmd/DeviceLoader/loadDevice?deviceName=${zdev}&devicePath=/Server/Linux"
done

