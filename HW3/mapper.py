#!/usr/bin/env python

import sys

result_list = []
output_format = {'key': None, 'value': [], 'PR': None}
for line in sys.stdin:
    line = line.strip()
    parse_line = line.split()

    output_format['key'] = parse_line[0]
    output_format['value'] = parse_line[1:-1]
    output_format['PR'] = None
    print "key=%s, value=%s" %(parse_line[0], ' '.join(parse_line[1:-1]))
   

    output_format['value'] = [parse_line[0]]
    PR = float(parse_line[-1])
    for key in parse_line[1:-1]:
        output_format['key'] = key
        output_format['PR'] = PR/len(parse_line[1:-1])
        print "key=%s, value=%s, %f" %(key, parse_line[0], PR/len(parse_line[1:-1]))
        
    

