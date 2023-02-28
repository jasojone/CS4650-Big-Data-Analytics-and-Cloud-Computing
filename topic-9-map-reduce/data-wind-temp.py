import re
import json

from mrjob.job import MRJob

QUALITY_RE = re.compile(r"[01459]")
from mrjob.job import MRJob

class Elevation(MRJob):

    def mapper(self, _, line):
        # extract fields from the line
        (usaf, wban, elev) = line.strip().split()
        # output weather station identifier as key and elevation as value
        yield f"{usaf}-{wban}", int(elev)

    def reducer(self, key, values):
        # get the minimum and maximum elevation for each weather station
        elevations = list(values)
        yield key, {
            "min_elev": min(elevations),
            "max_elev": max(elevations)
        }
        
if __name__ == '__main__':
    Elevation.run()
