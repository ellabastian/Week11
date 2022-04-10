from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField

class BasicForm(FlaskForm):
    first_name = StringField("First Name")
    email = StringField("Email")
    date_of_birth = DateField("Date of Birth")
    favourite_character = SelectField("Favourite Character", choices = ["Geralt", "Jennifer", "Ciri", "Dandelion aka The Bard", "Fringilla Vigo", "Triss", "Tissai", "Cahir", "Istredd", "Vesemir"])
    submit = SubmitField("Add Details")