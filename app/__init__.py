import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    os.makedirs(app.instance_path, exist_ok=True)

    # when i migrate, i'll use this
    #export DATABASE_URL="mysql+pymysql://USER:PASSWORD@HOST:3306/DBNAME"

    default_sqlite = "sqlite:///" + os.path.join(app.instance_path, "hotel.db")
    app.config.update(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev"),
        SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL", default_sqlite),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    db.init_app(app)
    login_manager.init_app(app)

    from . import routes  # noqa
    app.register_blueprint(routes.bp)

    with app.app_context():
        from . import models  # noqa
        db.create_all()

    return app

@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))
