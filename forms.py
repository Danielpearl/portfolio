from flask import *
from flask_wtf import Form
from wtforms import StringField, TextField, TextAreaField, SubmitField, validators

class ContactForm(Form):
    name = TextField("Name",  [validators.Required("Please enter your name.")])
    email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    subject = TextField("Subject",  [validators.Required("Please enter a subject.")])
    message = TextAreaField("Message",  [validators.Required("Please enter a message.")])
    submit = SubmitField("Send")
