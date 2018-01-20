import time
import re
import csv
import requests
from bs4 import BeautifulSoup

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z']

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

with open("nachnamen.csv", mode="w", newline="") as file:
    csv_writer = csv.writer(file, delimiter=" ")

    for i in range(0, 24):
        #try:
            page = requests.get('http://www.die-waldmanns.de/surnames/names-' + alphabet[i] + '.htm')

            soup = BeautifulSoup(page.text, "html.parser")
            names = soup.find_all('b')
            
            for name in names:
                if not name.text.strip() in map(str.upper, alphabet):
                # if name.text.strip():
                    if is_ascii(name.text):
                        csv_writer.writerow([name.text[:-4].strip()])
                    else:
                        print("fuck: " + name.text)
                        csv_writer.writerow([re.escape(name.text[:-4].strip())])
                else:
                    print("NO")

            # print(format((i / 1756), '.4f'))
            print(str(i) + " von 25 Seiten gekratzt")

            time.sleep(0.5)
        #except:
            #print("FUUUUUUUUCK")
            #time.sleep(100)

