#!/usr/bin/env python

import sys
import collections

pg_dict = {}
answer_dict = collections.OrderedDict()

for line in sys.stdin:
    line = line.strip()
    line_array = line.split(', ')
    if len(line_array) > 2:
        # ordinary ones
        key, value, PR = line_array
        key = key.split('=')[1]
        PR = float(PR)
        if key not in answer_dict:
            if key not in pg_dict:
                pg_dict[key] = PR
            else:
                pg_dict[key] += PR
        else:
            answer_dict[key][1] += PR
    else:
        # one's without PR
        key, value = line_array
        key = key.split('=')[1]
        value = value.split('=')[1]
        if key not in answer_dict:
            if key in pg_dict:
                answer_dict[key] = [value, pg_dict[key]]
            else:
                answer_dict[key] = [value, 0]
        else:
            raise Exception('I know Python!')

for item in answer_dict.items():
    print '%s %s %f' % (item[0], item[1][0], item[1][1])
