import csv
import random
from datetime import datetime

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


def random_line(file_location):
    with open(file_location, mode="r") as file:
        rand_line = random.randint(0, len(file.readlines()))

    with open(file_location, mode="r") as file:
        lines = list(read_my_lines(file, [rand_line]))
        try:
            return lines[0]
        except:
            random_line(file_location)


def generate_birthdate(min_yrs, max_yrs):
    year = random.choice(range(min_yrs, max_yrs))
    month = random.choice(range(1, 13))
    day = random.choice(range(1, 29))
    if month == 3:
        day = random.choice(range(1, 26))
    return(datetime(year, month, day))


def rand_phone(prefix, want_sep):
    n = '0000000000'
    c = 0
    while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==n[9]:
        if c > 100:
            break
        print("One fuck is ok")
        n = prefix + str(random.randint(10**9, 10**10-1))[3:]
        c += 1
    if want_sep:
        return n[:4] + '-' + n[4:]
    return n[:3] + n[3:]


if __name__ == "__main__":
    print(random_line("vornamen_w.csv"))
    print(generate_birthdate(1957, 2003))
    print(rand_phone("160"))
