from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, DateField,
    IntegerField, SubmitField
)
from wtforms.validators import (
    DataRequired, Email, EqualTo,
    Length, NumberRange
)


# Booking form 
class BookingForm(FlaskForm):
    start_date = DateField("Check-in",  validators=[DataRequired()])
    end_date   = DateField("Check-out", validators=[DataRequired()])
    guests     = IntegerField(
        "Guests",
        validators=[DataRequired(), NumberRange(min=1, max=6)]
    )
    submit     = SubmitField("Confirm booking")


# Registration from
class RegisterForm(FlaskForm):
    name     = StringField("Name",  validators=[DataRequired()])
    email    = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=6)]
    )
    confirm  = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), EqualTo('password')]
    )
    submit   = SubmitField("Register")


# Login form
class LoginForm(FlaskForm):
    email    = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit   = SubmitField("Log In")
