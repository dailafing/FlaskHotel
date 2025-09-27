import os
from flask import Flask, render_template
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

    app.config.from_object('instance.config.Config')

    db.init_app(app)
    login_mgr.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    login_mgr.login_view = "main.login" # redirect Unauthenticated users

    from . import routes, models  # im improting models so migrations see them
    app.register_blueprint(routes.bp)

    # register the deploy webhook
    from .deployhook import blueprint as deploy_blueprint
    app.register_blueprint(deploy_blueprint)

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template("500.html"), 500

    return app

@login_mgr.user_loader
def load_user(user_id: int):
    from .models import User
    return User.query.get(int(user_id))
