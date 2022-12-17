INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, "r") as inp:
        with open(OUTPUT_FILE, "w") as out:
            for line in inp:
                out.write(str.upper(line))


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
