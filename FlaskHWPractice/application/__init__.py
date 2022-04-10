from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:testpass@localhost/testdb'

from application import routes