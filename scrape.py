import time
import csv
import requests
from bs4 import BeautifulSoup

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

with open("vornamen_w.csv", mode="w", newline="") as file:
    csv_writer = csv.writer(file, delimiter=" ")

    for i in range(1, 1756):
        page = requests.get('http://www.firstname.de/Namenssuche/' + str(i) + '/0/alle/0/0/0/0/0/')

        soup = BeautifulSoup(page.text, "html.parser")
        girls = soup.find_all('a', {"class": "girl"})
        
        for girl in girls:
            if is_ascii(girl.text):
                csv_writer.writerow([girl.text.strip()])
            else:
                print("fuck")
        
        print(str(i // 1756) + "%")

        time.sleep(0.5)
