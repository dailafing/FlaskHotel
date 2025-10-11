from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, DateField,
    IntegerField, SubmitField
)
from wtforms.validators import (
    DataRequired, Email, EqualTo,
    Length, NumberRange
)


# Booking form with date and guest validation
class BookingForm(FlaskForm):
    """Form for creating and editing room bookings."""
    start_date = DateField("Check-in",  validators=[DataRequired()])
    end_date   = DateField("Check-out", validators=[DataRequired()])
    guests     = IntegerField(
        "Guests",
        validators=[DataRequired(), NumberRange(min=1, max=6)]
    )
    submit     = SubmitField("Confirm booking")


# Registration form with email and password validation
class RegisterForm(FlaskForm):
    """Form for user registration with password confirmation."""
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


# Login form with email validation
class LoginForm(FlaskForm):
    """Form for user authentication."""
    email    = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit   = SubmitField("Log In")
