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


# Factory function for creating Flask application instance
def create_app():
    """Create and configure Flask application with all extensions."""
    app = Flask(__name__, instance_relative_config=True)
    os.makedirs(app.instance_path, exist_ok=True)

    # Load configuration from instance folder
    app.config.from_object('instance.config.Config')

    # Initialize all Flask extensions
    db.init_app(app)
    login_mgr.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # Set login view for unauthenticated users
    login_mgr.login_view = "main.login"

    # Import and register blueprints
    from . import routes, models  # importing models so migrations see them
    app.register_blueprint(routes.bp)

    # Register deployment webhook for automatic updates
    from .deployhook import blueprint as deploy_blueprint
    app.register_blueprint(deploy_blueprint)

    # Custom error handlers for better user experience
    @app.errorhandler(404)
    def not_found_error(error):
        """Handle 404 errors with custom template."""
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors with custom template."""
        return render_template("500.html"), 500

    return app

@login_mgr.user_loader
def load_user(user_id: int):
    """Load user from database for Flask-Login session management."""
    from .models import User
    return User.query.get(int(user_id))
