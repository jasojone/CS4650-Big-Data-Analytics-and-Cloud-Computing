import re
import json

from mrjob.job import MRJob

QUALITY_RE = re.compile(r"[01459]")

class HourlyWindDirTemp(MRJob):

    def mapper(self, _, line):
        val = line.strip()
        (year, month, day, hour, wind_dir, temp, q) = (
            val[15:19], val[19:21], val[21:23], val[23:25], val[60:63], val[87:92], val[92:93])
        if (temp != "+9999" and re.match(QUALITY_RE, q)):
            yield wind_dir, {"low": int(temp), "high": int(temp), "count": 1}

    def reducer(self, key, values):
        temps = [value["low"] for value in values]
        low = min(temps) if temps else None
        high = max(temps) if temps else None
        count = len(temps)
        yield key, {"low": low, "high": high, "count": count}

if __name__ == '__main__':
    HourlyWindDirTemp.run()
