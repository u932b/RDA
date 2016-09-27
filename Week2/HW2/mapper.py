#!/usr/bin/env python

import sys

search_targets = ["chicago", "dec", "java", "hackathon"]

for line in sys.stdin:
    line = line.strip().lower()
    for target in search_targets:
        if target in line:
            print '%s\t%s' % (target, 1)
