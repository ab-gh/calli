import json
import inflect
import datetime as dt
from dateutil import tz

def pretty(content):
    p = inflect.engine()
    print(content)
    content = json.loads(content)
    print(f"{p.no('event', len(content))} today")
    for row in content:
        if row["type"] == "E":
            utc = dt.datetime.utcfromtimestamp(int(row['start']))
            print(local)
            print(f"{row['eventhex'].lower()} -> {local.strftime('%I:%M%p')} {row['name']}")