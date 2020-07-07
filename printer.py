import json
import inflect
import datetime as dt
from dateutil import tz

def pretty(content, range):
    p = inflect.engine()
    content = json.loads(content)
    print(f"{p.no('event', len(content))} {range}")
    for row in content:
        if row["type"] == "E":
            pointy = "->"
        elif row["type"] == "R":
            pointy = "-*"
        else:
            pointy = "-?"
        local = dt.datetime.utcfromtimestamp(int(row['start'])).replace(tzinfo=dt.timezone.utc).astimezone(tz.tzlocal())
        print(f"{row['eventhex'].lower()} {pointy} {local.strftime('%a %d %b %y')} {local.strftime('%I:%M %p')} {row['name']}")