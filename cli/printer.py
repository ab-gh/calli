import json
import inflect

def pretty(content):
    p = inflect.engine()
    content = json.loads(content)
    print(f"{p.no('event', len(content))} today")
    for row in content:
        if row["type"] == "E":
            print(f"{row['eventhex'].lower()} -> {row['start']} {row['name']}")