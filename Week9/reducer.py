#!/usr/bin/env python

import sys
import re

current_key = None
current_max = -1
current_min = -1
max_value = 0
min_value = 0
word = None
last_value = None
# max_value = -1
# min_value = -1

for line in sys.stdin:
    # print line
    line = line.strip()
    line_array = re.split('\t|,\ ', line)
    # print line_array
    # if len(line_array) > 2:
    #     # ordinary ones
    key, value = line_array
    key = key.split('=')[1]
    value = value.split('=')[1]
    global current_min
    global current_max
    if value.isdigit():
        if current_min == -1:
            current_min = value
        if current_max == -1:
            current_max = value
    else:
        value = len(value)
        if current_min == -1:
            current_min = value
        if current_max == -1:
            current_max = value
    # else:
    #     # one's without PR
    #     key, value = line_array
    #     key = key.split('=')[1]
    #     value = value.split('=')[1]
    #     if current_value:
    #         # already a value inside
    #         # print current_key, current_value
    #         last_value = current_value.pop()
    #     current_value.append(value)
    #     # print current_key, current_value
    #     PR = 0

    if current_key == key:
        global max_value
        global min_value
        max_value = max(current_max, value)
        min_value = min(current_min, value)
    else:
        print '%s %s ' % (current_key, (max_value, min_value))
        current_key = key
        current_max = -1
        current_min = -1
    #     current_PR = PR
    #     if PR == 0:
if current_key == key:
    print 'last_shit:', current_key
    print '%s %s ' % (current_key, (current_max, current_min))
