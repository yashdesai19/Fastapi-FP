# import json

# x = [1, "simple", "list"]

# json_string = json.dumps(x)
# print(json_string)

import json

data = {
    "name": "Yash",
    "age": 20,
    "skills": ["Python", "Git", "SQL"]
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f)
