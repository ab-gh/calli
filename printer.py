import json
import inflect
import datetime as dt
from dateutil import tz

def pretty(content):
    p = inflect.engine()
    content = json.loads(content)
    print(f"{p.no('event', len(content))} today")
    for row in content:
        if row["type"] == "E":
            pointy = "->"
        elif row["type"] == "R":
            pointy = "-*"
        else:
            pointy = "-?"
        utc = dt.datetime.utcfromtimestamp(int(row['start']))
        local = utc.replace(tzinfo=dt.timezone.utc).astimezone(tz=None)
        print(f"{row['eventhex'].lower()} {pointy} {local.strftime('%I:%M%p')} {row['name']}")