from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import date
from .models import Room, Booking
from . import db
from .forms import BookingForm

bp = Blueprint("main", __name__)

@bp.route("/flash-test")
def flash_test():
    flash("This is a test success message.", "success")
    flash("This is a test warning.", "warning")
    return redirect(url_for("main.index"))

@bp.route("/")
def index():
    rooms = Room.query.all()
    return render_template("index.html", rooms=rooms)

@bp.route("/rooms/<int:room_id>/book", methods=["GET", "POST"])
def book_room(room_id):
    room = Room.query.get_or_404(room_id)
    form = BookingForm()

    if form.validate_on_submit():
        s, e = form.start_date.data, form.end_date.data
        if s >= e:
            flash("Check‑out must be after check‑in.", "danger")
            return render_template("book.html", room=room, form=form)

        overlap = Booking.query.filter(
            Booking.room_id == room.id,
            Booking.start_date < e,
            s < Booking.end_date
        ).first()

        if overlap:
            flash("Sorry, those dates are not available.", "warning")
            return render_template("book.html", room=room, form=form)

        booking = Booking(
            user_id=1,  # temporary until I add auth
            room_id=room.id,
            start_date=s,
            end_date=e
        )
        db.session.add(booking)
        db.session.commit()
        flash("Booking confirmed!", "success")
        return redirect(url_for("main.my_bookings"))

    if request.method == "GET":
        form.start_date.data = date.today()
        form.end_date.data = date.today()
    return render_template("book.html", room=room, form=form)

@bp.route("/my-bookings")
def my_bookings():
    bookings = Booking.query.order_by(Booking.start_date.desc()).all()
    return render_template("my_bookings.html", bookings=bookings)

@bp.route("/contact")
def contact():
    return render_template("contact.html")
