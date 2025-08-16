import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


# Initialise extension singletons
db          = SQLAlchemy()     # ORM
login_mgr   = LoginManager()   # handles user sessions
migrate     = Migrate()        # handles Alembic migrations
bcrypt      = Bcrypt()         # hashes / verifies passwords


# Factory function
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
    login_mgr.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    login_mgr.login_view = "main.index" # redirect Unauthenticated users

    from . import routes, models  # im improting models so migrations see them
    app.register_blueprint(routes.bp)

    return app

@login_mgr.user_loader
def load_user(user_id: int):
    from .models import User
    return User.query.get(int(user_id))
