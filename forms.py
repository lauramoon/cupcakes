from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.fields.html5 import URLField
from wtforms.validators import InputRequired, NumberRange, Optional

class CupcakeAddForm(FlaskForm):
    """Form for adding a cupcake to the database"""
    flavor = StringField("Flavor", validators=[
                       InputRequired(message="Flavor cannot be blank")])
    size = StringField("Size", validators=[
                       InputRequired(message="Size cannot be blank")])
    rating = IntegerField("Rating", validators=[Optional(), 
                       NumberRange(min=1, max=10, message='Please enter a whole number between 1 and 10')])
    image = URLField("Photo Link", validators=[Optional()])