import csv
import string

with open("raw", 'r') as raw:
        for line in raw.readlines():
            try:
                print(line[:line.index(" ")].strip())
            except:
                print(line.strip())
