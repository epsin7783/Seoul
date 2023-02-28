#!/bin/bash

eval "cp /home/bit/Seoul/log/logfile4.log /home/bit/logfile4.log"

eval "hdfs dfs -put /home/bit/logfile4.log /input/"

exit 0
