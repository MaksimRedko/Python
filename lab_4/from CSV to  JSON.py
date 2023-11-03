import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as input_file:
        res = [kv for kv in csv.DictReader(input_file, delimiter=",", quotechar="\n")]

    with open(OUTPUT_FILENAME, "w") as output_file:
        json.dump(res, output_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")