import re
import json
from mrjob.job import MRJob

class MRMaxColMinRow(MRJob):

    def mapper(self, _, line):
        line = line.strip()
        line = line.split(',')
        yield line[0], int(line[2])

    def reducer(self, key, values):
        yield key, max(values)
        
if __name__ == '__main__':
    MRMaxColMinRow.run()