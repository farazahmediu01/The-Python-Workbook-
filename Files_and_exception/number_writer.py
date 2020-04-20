import json
numbers = list(range(2, 21, 2))


file_name = "numbers.json"
with open(file_name, "w") as f:
    json.dump(numbers, f)
