import re
import json

from mrjob.job import MRJob

QUALITY_RE = re.compile(r"[01459]")

monthName = ["Jan-", "Feb-", "Mar-", "Apr-", "May-", "Jun-",
            "Jul-", "Aug-", "Sep-", "Oct-", "Nov-", "Dec-"];

class MaxMonthlyTemperature(MRJob):
    
    def mapper(self, _, line):
        val = line.strip()
        (year, month, temp, q) = (val[15:19], val[20:21], val[87:92], val[92:93])
        if (temp != "+9999" and re.match(QUALITY_RE, q)):
            yield monthName[int(month) - 1] + str(year), int(temp)

    def reducer(self, key, values):
        yield key, max(values)

if __name__ == '__main__':
    MaxMonthlyTemperature.run()
