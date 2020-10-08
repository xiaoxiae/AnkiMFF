import json
import os

deck_name = os.path.join(os.path.dirname(__file__), "deck.json")

def recursive_deck_sort(d):
    if isinstance(d, dict):
        for k, v in d.items():
            if k == "children":
                v.sort(key=lambda a: a["name"])

            if isinstance(v, list):
                for i in v:
                    recursive_deck_sort(i)

with open(deck_name, "r") as f:
    c = json.loads(f.read())
    recursive_deck_sort(c)

with open(deck_name, "w") as f:
    f.write(json.dumps(c, sort_keys=True, indent=4))
