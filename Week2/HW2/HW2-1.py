#!/usr/bin/env python

import sys

search_targets = ["chicago", "dec", "java", "hackathon"]
target_dict = dict((key, 0) for key in search_targets)

for line in sys.stdin:
    line = line.strip().lower()
    for target in search_targets:
        if target in line:
            target_dict[target] = target_dict.get(target) + 1

print "Chicago ", target_dict["chicago"]
print "Dec ", target_dict["dec"]
print "Java ", target_dict["java"]
print "hackathon ", target_dict["hackathon"]
