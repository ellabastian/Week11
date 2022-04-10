from flask import render_template, request, url_for

from application import app

@app.route("/")
@app.route("/home")
def home():
    url = url_for("cast")
    url2 = url_for("episodes")
    return render_template("home.html", title = "Home", page_title = url, page_title2 = url2)

@app.route("/cast")
def cast():
    url2 = url_for("episodes")
    url3 = url_for("home")
    directors = ["E1,2,7: Alik Sakharov", "E3,4: Alex Garcia Lopez", "E5,6: Charlotte Brändström", "E7,8: Marc Jobst",
                    "E9, 10: Stephen Surjik", "E11,12: Sarah O'Gorman", "E13: Ed Bazalgette", "E14,15: Louise Hooper", "E16: Ed Bazalgette"]
    return render_template("cast.html", title = "Cast", person= directors, page_title2 = url2, page_title3 = url3)

@app.route("/episodes")
def episodes():
    url3 = url_for("home")
    url = url_for("cast")
    return render_template("episodes.html", title = "Episodes", page_title3 = url3, page_title = url)