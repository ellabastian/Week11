from flask import render_template, request, url_for

from application import app

from application.forms import BasicForm

@app.route("/")
@app.route("/home")
def home():
    url = url_for("cast")
    url2 = url_for("episodes")
    url4 = url_for("form")
    return render_template("home.html", title = "Home", page_title = url, page_title2 = url2, page_title4 = url4)

@app.route("/cast")
def cast():
    url2 = url_for("episodes")
    url3 = url_for("home")
    url4 = url_for("form")
    directors = ["E1,2,7: Alik Sakharov", "E3,4: Alex Garcia Lopez", "E5,6: Charlotte Brändström", "E7,8: Marc Jobst",
                    "E9, 10: Stephen Surjik", "E11,12: Sarah O'Gorman", "E13: Ed Bazalgette", "E14,15: Louise Hooper", "E16: Ed Bazalgette"]
    return render_template("cast.html", title = "Cast", person= directors, page_title2 = url2, page_title3 = url3, page_title4 = url4)

@app.route("/episodes")
def episodes():
    url3 = url_for("home")
    url = url_for("cast")
    url4 = url_for("form")
    return render_template("episodes.html", title = "Episodes", page_title3 = url3, page_title = url, page_title4 = url4)

@app.route("/form", methods=["GET", "POST"])
def form():
    url3 = url_for("home")
    url = url_for("cast")
    url2 = url_for("episodes")
    error = ""
    form = BasicForm()

    if request.method == "POST":
        first_name = form.first_name.data
        email = form.email.data
        date_of_birth = form.date_of_birth.data
        favourite_character = form.favourite_character.data

        if len(first_name) == 0 or len(email) == 0 or len(date_of_birth) == 0 or len(favourite_character) == 0:
            error = "Please enter the required input"
        else:
            return "Thank you"

    return render_template("form.html", form=form, message=error, title="Form", page_title3 = url3, page_title = url, page_title2 = url2)