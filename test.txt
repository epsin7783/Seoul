#!/bin/bash

eval "cp /home/bit/Seoul/log/logfile2.log /home/bit/logfile2.log"

eval "hdfs dfs -put /home/bit/logfile2.log /input"

eval "python3 /home/bit/test2_pyspark.py"

eval "hdfs dfs -getmerge /input/logfiletest /home/bit/test119.csv"

eval "mv /home/bit/test119.csv /home/bit/flume"

#eval "sqoop export --connect jdbc:mysql://localhost:3306/seoul --username bit --password 1234 -m 1 --table main_pyspark --update-key id --update-mode updateonly --export-dir hdfs://master:10000/input/flume --columns 'id,name,day,time,prediction'"
eval "sqoop export --connect jdbc:mysql://localhost:3306/seoul --username bit --password 1234 -m 1 --table main_pyspark --export-dir hdfs://master:10000/input/flume --columns 'id,name,day,time,prediction'"

eval "hdfs dfs -rm -f /inputlogfiletest/*"
eval "hdfs dfs -rm -f /input/flume/*"
eval "hdfs dfs -rm -f /input/logfile2.log"
eval "rm -f /home/bit/flume/*"
eval "rm -f /home/bit/logfile2.log"

exit 0
