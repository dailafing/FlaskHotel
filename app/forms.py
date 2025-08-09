from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class BookingForm(FlaskForm):
    start_date = DateField("Check‑in", validators=[DataRequired()])
    end_date   = DateField("Check‑out", validators=[DataRequired()])
    guests     = IntegerField("Guests", validators=[DataRequired(), NumberRange(min=1, max=6)])
    submit     = SubmitField("Confirm booking")
