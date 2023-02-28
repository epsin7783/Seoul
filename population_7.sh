#!/bin/bash

eval "hdfs dfs -rm -r /input/logfiletest/*"

eval "hdfs dfs -rm -r /input/flume/*"

eval "hdfs dfs -rm -r /input/logfile4.log"

eval "rm -f /home/bit/flume/*"

eval "rm -f /home/bit/logfile4.log"

eval "rm -f /home/bit/test119.csv"

exit 0
