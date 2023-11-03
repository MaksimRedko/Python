import json

INPUT_FILE = "input.json"


def task() -> float:
    with open(INPUT_FILE, "r") as input_file:
        json_input_file = json.load(input_file)
    res = sum(i["score"] * i["weight"] for i in json_input_file)
    return round(res, 3)


print(task())
