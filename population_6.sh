#!/bin/bash

eval "sqoop export --connect jdbc:mysql://localhost:3306/seoul --username bit --password 1234 -m 1 --table main_pyspark --update-key name,day,time --update-mode updateonly --export-dir hdfs://master:10000/input/flume --columns 'id,name,day,time,prediction'"

exit 0
