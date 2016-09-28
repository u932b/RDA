#!/usr/bin/env python

from mrjob.job import MRJob
import re


class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        output_format = {'key': None, 'value': [], 'PR': None}
        line = line.strip()
        parse_line = line.split()
        output_format['key'] = parse_line[0]
        output_format['value'] = parse_line[1:-1]
        output_format['PR'] = None
        print "key=%s\tvalue=%s" % (parse_line[0], ' '.join(parse_line[1:-1]))
        output_format['value'] = [parse_line[0]]
        PR = float(parse_line[-1])
        for key in parse_line[1:-1]:
            output_format['key'] = key
            output_format['PR'] = PR / len(parse_line[1:-1])
            print "key=%s\tvalue=%s, %f" % (key, parse_line[0], PR /
                                            len(parse_line[1:-1]))

    def reducer(self, key, value):
        current_key = None
        current_value = []
        current_PR = 0
        last_value = None

        value_array = re.split(',\ ', value)
        if len(value_array) > 1:
            # ordinary ones
            key = key.strip().split('=')[1]
            value = value_array[0].split('=')[1]
            PR = float(value_array[1])
        else:
            # one's without PR
            key = key.strip().split('=')[1]
            value = value_array[0].split('=')[1]
            if current_value:
                # already a value inside
                last_value = current_value.pop()
            current_value.append(value)
            PR = 0
        if current_key == key:
            current_PR += PR
        else:
            if current_key:
                if last_value:
                    print '%s %s %f' % (current_key, last_value, current_PR)
                    last_value = None
                    current_value.pop()
                else:
                    print '%s %s %f' % (current_key, current_value.pop(),
                                        current_PR)
            current_key = key
            current_PR = PR
            if PR == 0:
                current_value.append(value)
        if current_key == key:
            print '%s %s %f' % (current_key, current_value.pop(), current_PR)
