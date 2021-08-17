from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, DataRequired

class ContactForm(FlaskForm):

    email = EmailField('Email', validators=[DataRequired(), Email()])
    message = StringField('Message', validators=[DataRequired()])

    submit = SubmitField('Send Message')