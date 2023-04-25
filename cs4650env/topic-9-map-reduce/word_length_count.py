import re
import json

from mrjob.job import MRJob

PUNC_RE = re.compile(r"[^a-z]")

class WordLengthFrequency(MRJob):

    def mapper(self, _, line):
        thelist = line.split()
        for x in thelist:
            y = x.lower()
            z = re.sub(PUNC_RE, '', y)
            w = len(z)
            if w > 3:
                yield w, {"example":z, "count":1}

    def reducer(self, key, values):
        example = ''
        count = 0
        for x in values:
            example = x["example"]
            count += x["count"]
        if len(example) > 0:
            yield key, {"example":example, "count":count}


if __name__ == '__main__':
    WordLengthFrequency.run()
