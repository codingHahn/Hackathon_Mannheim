import requests
import random

from bs4 import BeautifulSoup
from filereader import random_line, generate_birthdate, rand_phone


def get_streets(plz, town_name):
    try:
        response = requests.get("http://www.maptier.de/suche.php?q=" + plz)
    except:
        return [random_line("strassen.csv") + " ! Gibt es nicht wirklich !"]

    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all("li")

    streets_str = None

    for result in results:
        res = result.find("a")
        if town_name in res.text:
            response = requests.get(res['href'] + "&s=")
            soup = BeautifulSoup(response.text, "html.parser")
            streets = soup.find_all("li")

            streets_str = []

            for street in streets:
                street = street.text[:street.text.index(" Plz:")]
                streets_str.append(street)
            break
    if streets_str is not None:
        return streets_str
    else:
        return ["Nothing found"]


def rand_street(plz, town_name):
    streets = get_streets(plz, town_name)
    street = streets[random.randint(0, len(streets) - 1)]
    return street


if __name__ == "__main__":
    print(rand_street("73463", "Westhausen"))
