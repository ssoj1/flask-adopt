"""Forms for adopt app."""

from wtforms import validators
from wtforms.fields.core import SelectField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import InputRequired, Optional
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.widgets.core import TextArea

class AddPet(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", 
                        validators=[InputRequired()])
    species = StringField("Species", 
                        validators=[InputRequired()])
    photo_url = StringField("Photo URL", 
                        validators=[InputRequired()])
    age = SelectField("Age", 
                choices = [('baby', 'Baby'), 
                            ('young', 'Young'), 
                            ('adult', 'Adult'), 
                            ('senior', 'Senior')],
                validators=[InputRequired()])
    notes = TextAreaField("Notes")
 
