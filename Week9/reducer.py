#!/usr/bin/env python

import sys
import re
import time
from datetime import datetime


current_key = None
current_max = -(sys.maxint)
current_min = sys.maxint
word = None
last_value = None


def isTimeFormat(input):
    try:
        time.strptime(input, '%Y-%m-%d %H:%M:%S.%f')
        return True
    except ValueError:
        return False

for line in sys.stdin:
    line = line.strip()
    line_array = re.split('\t|,\ ', line)
    # print line_array
    # if len(line_array) > 2:
    #     # ordinary ones
    key, value = line_array
    key = key.split('=')[1]
    if not current_key:
        current_key = key
    value = value.split('=')[1]
    global current_min
    global current_max
    if value.isdigit():
        pass
    elif isTimeFormat(value):
        value = datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f').strftime('%s')
    else:
        value = len(value)

    if current_key == key:
        current_max = max(int(current_max), int(value))
        current_min = min(int(current_min), int(value))
    else:
        print '%s %s ' % (current_key, (current_max, current_min))
        current_key = key
        current_max = -(sys.maxint)
        current_min = sys.maxint

if current_key == key:
    current_max = max(int(current_max), int(value))
    current_min = min(int(current_min), int(value))
    print '%s %s ' % (current_key, (current_max, current_min))
