"""Forms for adopt app."""
from wtforms.fields.core import BooleanField
from wtforms.validators import InputRequired, AnyOf, Optional, URL
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name",
                       validators=[InputRequired()])
    species = SelectField("Species",
                            validators=[InputRequired()],
                            choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])
    age = SelectField("Age",
                      choices=[('baby', 'Baby'),
                               ('young', 'Young'),
                               ('adult', 'Adult'),
                               ('senior', 'Senior')],
                      validators=[InputRequired()])
    notes = TextAreaField("Notes")


class EditPetForm(FlaskForm):
    """Edit pet details."""

    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Availability")
