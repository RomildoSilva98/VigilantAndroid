#!/bin/bash

netstat -tpan|grep "ESTABLISHED"|cut -d":" -f2|cut -d" " -f6 > ips.txt