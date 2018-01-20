import csv
import random

def read_my_lines(csv_reader, lines_list):
    # make sure every line number shows up only once:
    lines_set = set(lines_list)
    for line_number, row in enumerate(csv_reader):
        if line_number in lines_set:
            yield row
            lines_set.remove(line_number)
            # Stop when the set is empty
            if not lines_set:
                raise StopIteration


def random_name(file_location):
    with open(file_location, mode="r") as file:
        rand_line = random.randint(0, len(file.readlines()))

    with open(file_location, mode="r") as file:
        lines = list(read_my_lines(file, [rand_line]))
        return lines[0]

if __name__ == "__main__":
    print(random_name("vornamen_w.csv"))
