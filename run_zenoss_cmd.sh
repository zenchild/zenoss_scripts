#!/bin/bash

. ./0ENV.sh  # add connection variables in here

zcmd=$1
curl -s -u "${ZUSER}:${ZPASS}" "http://${ZSERVER}/zport/dmd/Devices/Server/Linux/TSM/devices/my.host.name/${zcmd}"
