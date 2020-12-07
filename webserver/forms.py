from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError


class ContactForm(FlaskForm):
    name = TextField("Name",
                     [validators.DataRequired("Please enter your name.")])
    email = TextField("Email", [
        validators.DataRequired("Please enter your email address."),
        validators.Email("Invalid email address")
    ])
    subject = TextField("Subject",
                        [validators.DataRequired("Please enter a subject")])
    message = TextAreaField(
        "Message", [validators.DataRequired("Please enter a message")])
    submit = SubmitField("Send") 