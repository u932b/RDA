#!/usr/bin/env python

import sys

current_key = None
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
        current_PR += float(PR)
    else:
        # one's without PR
        key, value = line_array
        current_key = key.split('=')[1]
        current_value = value.split('=')[1]
print '%s %s %f' % (current_key, current_value, current_PR)
