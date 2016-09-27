#!/usr/bin/env python

import sys

search_targets = ["chicago", "dec", "java", "hackathon"]

target_dict = dict((key, 0) for key in search_targets)
# not compatible with 2.6
# target_dict = {key: 0 for key in search_targets}

for line in sys.stdin:
    line = line.strip()

    # parse the input we got from mapper.py
    try:
        word, count = line.split('\t', 1)
    except:
        # ignore cases where words are missing
        continue

    count = int(count)

    if target_dict.get(word) is not None:
        target_dict[word] = target_dict.get(word) + count

print "Chicago ", target_dict["chicago"]
print "Dec ", target_dict["dec"]
print "Java ", target_dict["java"]
print "hackathon ", target_dict["hackathon"]
