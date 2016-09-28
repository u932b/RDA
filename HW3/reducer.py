#!/usr/bin/env python

import sys
import collections

current_key = None
current_value = []
current_PR = 0
word = None
last_value = None
answer_dict = collections.OrderedDict()

for line in sys.stdin:
    line = line.strip()
    line_array = line.split(', ')
    if len(line_array) > 2:
        # ordinary ones
        key, value, PR = line_array
        key = key.split('=')[1]
        value = value.split('=')[1]
        PR = float(PR)
        if key not in answer_dict:
            answer_dict[key] = [None, PR]
        else:
            answer_dict[key][1] += PR
    else:
        # one's without PR
        key, value = line_array
        key = key.split('=')[1]
        value = value.split('=')[1]
        PR = 0
        if key not in answer_dict:
            answer_dict[key] = [value, PR]
        else:
            answer_dict[key][0] = value

for item in answer_dict.items():
    print '%s %s %f' % (item[0], item[1][0], item[1][1])
