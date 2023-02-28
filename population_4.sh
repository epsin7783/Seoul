#!/bin/bash

eval "hdfs dfs -getmerge /input/logfiletest/part* /home/bit/test119.csv"

exit 0
