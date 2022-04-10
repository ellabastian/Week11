from flask import render_template, url_for

from application import app

# from application.forms import BasicForm

@app.route('/')
@app.route('/home')
def home():
    url = url_for('cast')
    url2 = url_for('episodes')
    url_name = 'Cast'
    url_name2 = 'Episodes'
    return render_template('home.html', title='Home', url=url,url_name=url_name, url2=url2, url_name2=url_name2)

@app.route('/cast')
def cast():
    url2 = url_for('episodes')
    url3 = url_for('home')
    url_name2 = 'Episode'
    url_name3 = 'Home'
    directors = ['Alik Sakharov - S1 EP1, S1, EP2, S1, EP7', 'Alex Garcia Lopez - S1 EP3, S1 EP4', 'Charlotte Brändström - S1 EP5, S1 EP6', 'Marc Jobst - S1 EP7, S1 EP8', 'Stephen Surjik - S2 EP1, S2, Ep2,', 'Sarah OGorman - S2 EP3, S1 Ep4', 'Ed Bazalgette - S2 EP5, S5 EP8', 'Louise Hooper - S2 EP6, S2, EP7']
    return render_template('cast.html', title='Cast', person=directors, url=url2,url_name=url_name2, url2=url3, url_name2=url_name3)

@app.route('/episodes')
def episodes():
    url = url_for('cast')
    url3 = url_for('home')
    url_name = 'Cast'
    url_name3 = 'Home'
    return render_template('episodes.html', title='Episodes', url=url, url_name=url_name, url2=url3, url_name2=url_name3)