from flask import Flask, request, render_template
import random

from filereader import random_name, generate_birthdate, rand_phone

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result')
def result():
    gender = request.args.get("gender")
    if gender == "m":
        firstname = random_name("vornamen_m.csv")
        picture = "/static/male.jpg"
    elif gender == "w":
        firstname = random_name("vornamen_w.csv")
        picture = "/static/female.jpg"
    place = random_name("plz-ort.csv").replace(",", " ")
    lastname = random_name("nachnamen.csv")
    birthdate = generate_birthdate(1957, 2003).strftime("%d.%m.%Y")

    cell_prefix = ["151", "160", "170", "171", "175", "152", "151", "162", "172", "173", "174", "157", "163", "177", "178", "159"]
    cellphone = rand_phone(cell_prefix[random.randint(0, len(cell_prefix) - 1)])
    landline = None

    return render_template("result.html", firstname=firstname, lastname=lastname, place=place, picture=picture, birthdate=birthdate, cellphone=cellphone, landline=landline)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
