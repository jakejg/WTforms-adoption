from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, URL, AnyOf, NumberRange, Optional

class AddPet(FlaskForm):

    name = StringField("Name of Pet", validators=[InputRequired()])
    species = StringField("Type of Animal", validators=[InputRequired(), AnyOf(["Cat", "Dog"], message="You must pick either Cat, Dog, or Porcupine")])
    photo_url = StringField("Picture of Pet (URL)", validators=[Optional(), URL()])
    age = IntegerField("Age of the Pet", validators=[InputRequired(), NumberRange(min=0, max=30, message="Is your pet really over 30?")])
    notes = StringField("Any Notes About the Pet")

class EditPet(FlaskForm):

    name = StringField("Name of Pet", validators=[InputRequired()])
    photo_url = StringField("Picture of Pet (URL)", validators=[Optional(), URL()])
    age = IntegerField("Age of the Pet", validators=[InputRequired(), NumberRange(min=0, max=30, message="Is your pet really over 30?")])
    notes = StringField("Any Notes About the Pet")
    available = BooleanField("Check Box if Still Available")
