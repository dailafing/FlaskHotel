from flask import Blueprint, render_template
from .models import Room

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    rooms = Room.query.all()
    return render_template("index.html", rooms=rooms)
