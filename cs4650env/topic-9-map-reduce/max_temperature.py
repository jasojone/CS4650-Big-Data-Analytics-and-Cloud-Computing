import re
import json

from mrjob.job import MRJob

QUALITY_RE = re.compile(r"[01459]")

class MaxTemperature(MRJob):

    def mapper(self, _, line):
        val = line.strip()
        (year, temp, q) = (val[15:19], val[87:92], val[92:93])
        if (temp != "+9999" and re.match(QUALITY_RE, q)):
            yield year, int(temp)

    def reducer(self, key, values):
        yield key, max(values)

if __name__ == '__main__':
    MaxTemperature.run()
