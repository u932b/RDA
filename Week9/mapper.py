#!/usr/bin/env python

import sys

result_list = []
# output_format = {'key': None, 'value': [], 'PR': None}
header = """id,station_id,status,available_bike_count,available_dock_count,created_at,station_summary_id
"""
header_list = header.rstrip().lstrip().split(',')
# print header_list
for line in sys.stdin:
    line = line.strip()
    parse_line = line.split(',')
    if parse_line[1] == header_list[1]:
        continue
    dic = dict(zip(header_list, parse_line))
    # output_format['key'] = parse_line[0]
    # output_format['value'] = parse_line[1:-1]
    # output_format['PR'] = None
    for key in dic.keys():
        print "key=%s\tvalue=%s" % (key, dic[key])

    # output_format['value'] = [parse_line[0]]
    # PR = float(parse_line[-1])
    # for key in parse_line[1:-1]:
    #     output_format['key'] = key
    #     output_format['PR'] = PR / len(parse_line[1:-1])
    #     print "key=%s\tvalue=%s, %f" % (key, parse_line[0], PR /
    #                                     len(parse_line[1:-1]))
    # print dic
