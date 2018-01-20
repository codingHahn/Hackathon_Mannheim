from flask import Flask, request, render_template
import random

from filereader import random_line, generate_birthdate

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result')
def result():
    gender = request.args.get("gender")
    if gender == "m":
        firstname = random_line("vornamen_m.csv")
        picture = "/static/male.jpg"
    elif gender == "w":
        firstname = random_line("vornamen_w.csv")
        picture = "/static/female.jpg"
    place = random_line("plz-ort.csv").replace(",", " ")
    lastname = random_line("nachnamen.csv")
    birthdate = generate_birthdate(1957, 2003).strftime("%d.%m.%Y")
    address = random_line("strassen.csv") + str(random.randint(1, 47))
    return render_template("result.html", firstname=firstname, lastname=lastname, address=address, place=place, birthdate=birthdate, picture=picture)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
