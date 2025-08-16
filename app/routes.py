from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user, login_user, logout_user
from datetime import date
from .models import Room, Booking, User
from . import db
from .forms import BookingForm, RegisterForm, LoginForm

bp = Blueprint("main", __name__)

# Main Routes

@bp.route("/flash-test")
def flash_test():
    flash("This is a test success message.", "success")
    flash("This is a test warning.", "warning")
    return redirect(url_for("main.index"))

@bp.route("/")
def index():
    rooms = Room.query.all()
    return render_template("index.html", rooms=rooms)

@bp.route("/contact")
def contact():
    return render_template("contact.html")



# Booking Routes

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
            user_id=current_user.id,
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
@login_required
def my_bookings():
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template("my_bookings.html", bookings=bookings)


@bp.route("/bookings/<int:booking_id>/edit", methods=["GET", "POST"])
def edit_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    form = BookingForm(obj=booking)

    if form.validate_on_submit():
        # Don't allow changing to overlapping dates
        overlapping = Booking.query.filter(
            Booking.room_id == booking.room_id,
            Booking.id != booking.id,
            Booking.start_date < form.end_date.data,
            form.start_date.data < Booking.end_date
        ).first()

        if overlapping:
            flash("Selected dates overlap with another booking.", "danger")
            return render_template("edit_booking.html", form=form, booking=booking)

        booking.start_date = form.start_date.data
        booking.end_date = form.end_date.data
        booking.guests = form.guests.data
        db.session.commit()
        flash("Booking updated.", "success")
        return redirect(url_for("main.my_bookings"))

    return render_template("edit_booking.html", form=form, booking=booking)


@bp.route("/bookings/<int:booking_id>/delete", methods=["POST"])
def delete_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    db.session.delete(booking)
    db.session.commit()
    flash("Booking cancelled.", "warning")
    return redirect(url_for("main.my_bookings"))



# Authenticatoin

@bp.route("/register", methods=["GET", "POST"])
def register():
    """Create a new user account."""
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash("Email is already registered.", "danger")
            return render_template("register.html", form=form)

        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash("Account created! Please log in.", "success")
        return redirect(url_for("main.login"))
    return render_template("register.html", form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    """Log the user in."""
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Logged in successfully.", "success")
            return redirect(request.args.get("next") or url_for("main.index"))
        flash("Invalid email or password.", "danger")
    return render_template("login.html", form=form)


@bp.route("/logout")
@login_required
def logout():
    """Log the user out."""
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("main.index"))


