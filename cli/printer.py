import json

def pretty(content):
    print(content)
    for row in json.loads(content):
        if row["type"] == "E":
            print(f"-> {row['start']} {row['name']}")