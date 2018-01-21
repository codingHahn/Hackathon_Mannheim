from flask import Flask, request, render_template
import random

from filereader import random_line, generate_birthdate, rand_phone


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result')
def result():
    print("Got request")
    gender = request.args.get("gender")
    if gender == "m":
        firstname = random_line("vornamen_m.csv")
        picture = "/static/male.jpg"
    elif gender == "w":
        firstname = random_line("vornamen_w.csv")
        picture = "/static/female.jpg"
    print("Got Name")
    place_and_landline = random_line("vorwahl_ganz.csv").split(",")
    print("got place_and_landline")
    place = place_and_landline[0] + " " + place_and_landline[1]
    landline = rand_phone(place_and_landline[2], False)
    print("Got landline")
    lastname = random_line("nachnamen.csv")
    print("Got last name")
    birthdate = generate_birthdate(1957, 2003).strftime("%d.%m.%Y")
    print("Got birthdate")

    address = random_line("strassen.csv") + str(random.randint(1, 47))
    print("Got Address")

    cell_prefix = ["151", "160", "170", "171", "175", "152", "151", "162", "172", "173", "174", "157", "163", "177", "178", "159"]
    cellphone = rand_phone("0" + cell_prefix[random.randint(0, len(cell_prefix) - 1)], True)
    print("Got cellphone")

    iban = random_line("iban.csv")
    print("Got IBAN")

    return render_template("result.html", firstname=firstname, lastname=lastname, address=address, place=place, picture=picture, birthdate=birthdate, cellphone=cellphone, landline=landline, iban=iban)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
