"""Forms for adopt app."""
from wtforms.validators import InputRequired, AnyOf, Optional, URL
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", 
                        validators=[InputRequired()])
    species = StringField("Species", 
                        validators=[InputRequired(), AnyOf(values=['cat','dog','porcupine'])])
                        # TODO: Uppercase cat, dog, porcupines are invalid
    photo_url = StringField("Photo URL", 
                        validators=[Optional(), URL()])
    age = SelectField("Age", 
                choices = [('baby', 'Baby'), 
                            ('young', 'Young'), 
                            ('adult', 'Adult'), 
                            ('senior', 'Senior')],
                validators=[InputRequired()])
    notes = TextAreaField("Notes", validators=[Optional()])