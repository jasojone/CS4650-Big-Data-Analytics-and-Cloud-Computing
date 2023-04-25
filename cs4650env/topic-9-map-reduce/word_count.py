import re

from mrjob.job import MRJob

PUNC_RE = re.compile(r"[^a-z]")

class WordFrequency(MRJob):

    def mapper(self, _, line):
        thelist = line.split()
        for x in thelist:
            y = x.lower()
            z = re.sub(PUNC_RE, '', y)
            yield z, 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    WordFrequency.run()
