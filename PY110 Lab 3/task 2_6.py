import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)

    return sorted(json_data, key=lambda item: item["length"])


if __name__ == "__main__":
    data = task()
    print(json.dumps(data, indent=4))

    output_file = "output.json"
    with open(output_file, "w") as o:
        json.dump(data, o, indent=4)
