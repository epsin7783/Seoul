#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    words= line.split()
    for word in words:
        value = 1
        print("%s\\t%d" % (word , value))

last_word = None
total_count = 0

for line in sys.stdin:
    line = line.strip()

    word, value = line.split("\\t", 1)
    value = int(value)

    if last_word == word:
        total_count += value

    else:
        if last_word:
            print("{0}\\t{1}".format(last_word , total_count ))

        total_count = value
        last_word = word

if last_word == word:
    print("{0}\\t{1}".format(last_word , total_count ))