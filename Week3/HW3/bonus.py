#!/usr/bin/env python

'''
MrPageLink

This class uses mrjob library to perform multistep MapReduce on PageRank input.

Local usage:
    python bonus.py input.txt
Hadoop usage:
    python bonus.py input.txt -r hadoop --hadoop-streaming-jar \
            /path/to/streaming/jar
'''


# https://github.com/Yelp/mrjob.git
from mrjob.job import MRJob
from mrjob.step import MRStep


class MRPageRank(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(mapper=self.mapper2,
                   reducer=self.reducer),
            MRStep(mapper=self.mapper2,
                   reducer=self.reducer2),
        ]

    def mapper(self, _, line):
        line = line.strip()
        parse_line = line.split()
        PR = float(parse_line[-1])
        PR = round(PR / len(parse_line[1:-1]), 6)
        yield (parse_line[0], [' '.join(parse_line[1:-1]), 0])
        for key in parse_line[1:-1]:
            yield (key, [parse_line[0], PR])

    def reducer(self, key, PR):
        sum = 0
        elements = ''
        listo = []
        for value in PR:
            listo.append(value)
            if value[1] == 0:
                elements = value[0]
            sum += value[1]
        yield (key + ' ' + elements, round(sum, 6))

    def mapper2(self, line, PR):
        line = line.strip()
        parse_line = line.split()
        PR = float(PR)
        PR = round(PR / len(parse_line[1:]), 6)
        yield (parse_line[0], [' '.join(parse_line[1:]), 0])
        for key in parse_line[1:]:
            yield (key, [parse_line[0], PR])

    def reducer2(self, key, PR):
        sum = 0
        elements = ''
        listo = []
        for value in PR:
            listo.append(value)
            if value[1] == 0:
                elements = value[0]
            sum += value[1]
        print key, elements, str(round(sum, 6))

if __name__ == '__main__':
    MRPageRank.run()
