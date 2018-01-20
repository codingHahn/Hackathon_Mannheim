import time
import re
import csv
import requests
from bs4 import BeautifulSoup

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z']

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

with open("vorwahl.csv", mode="w", newline="") as file:
    with open("plz-ort.csv", 'r') as plz:
        csv_writer = csv.writer(file, delimiter=" ")

        for i in plz.readlines():
            v = i[:i.index(',')]
            print(v)
            page = requests.post('http://www.postleitzahlenbuch.info/postleitzahlen.html', data={"plz": str(v), "res": 1}, headers={"user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0"})

            soup = BeautifulSoup(page.text, "html.parser")

            try:
                vorwahl = soup.find(text="Vorwahl:").findNext("td")
                print("bitte " + vorwahl.text.strip())

                file.write(i.strip() + "," + vorwahl.text.strip() + "\n")
            except:
                print("No ZIP code was found for " + v)
