#!/usr/bin/env python

import sys

current_key = None
current_value = []
current_PR = 0
word = None
real_value = None

for line in sys.stdin:
    line = line.strip()
    line_array = line.split(', ')
    if len(line_array) > 2:
        # ordinary ones
        key, value, PR = line_array
        key = key.split('=')[1]
        value = value.split('=')[1]
        PR = float(PR)
    else:
        # one's without PR
        key, value = line_array
        key = key.split('=')[1]
        value = value.split('=')[1]
        if current_value:
            # already a value inside
            # print current_key, current_value
            real_value = current_value.pop()
        current_value.append(value)
        # print current_key, current_value
        PR = 0
    if current_key == key:
        current_PR += PR
    else:
        if current_key:
            if real_value:
                print '%s %s %f' % (current_key, real_value, current_PR)
                real_value = None
                current_value.pop()
            else:
                print '%s %s %f' % (current_key, current_value.pop(), current_PR)
        current_key = key
        current_PR = PR
        if PR == 0:
            current_value.append(value)
try:
    if current_key == key:
        print '%s %s %f' % (current_key, current_value.pop(), current_PR)
except:
    pass
