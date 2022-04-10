from flask import Flask

#creaet new instance of FLask
app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:testpass@localhost/testdb'

from application import routes