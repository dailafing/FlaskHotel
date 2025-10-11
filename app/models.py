from . import db, bcrypt
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    """User model for authentication and user management."""
    __tablename__ = "user"
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(100), nullable=False)
    email         = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role          = db.Column(db.String(20), default="guest")

    # Password helpers - secure password handling using bcrypt
    def set_password(self, password: str) -> None:
        """Hash raw password and store it securely.
        
        Uses bcrypt to generate a salted hash that cannot be reversed.
        bcrypt automatically generates a random salt for each password,
        making rainbow table attacks ineffective. The hash is stored as 
        a UTF-8 string in the database, never storing the plain text password.
        
        Args:
            password (str): The plain text password to hash
        """
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password: str) -> bool:
        """Verify raw password against stored hash.
        
        Compares the provided password with the stored hash using bcrypt.
        bcrypt handles the salt extraction and comparison automatically,
        providing constant-time comparison to prevent timing attacks.
        
        Args:
            password (str): The plain text password to verify
            
        Returns:
            bool: True if password matches, False otherwise
        """
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.email}>"


class Room(db.Model):
    """Room model representing available accommodation."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255))

    def __repr__(self):
        return f"<Room {self.name}>"

class Booking(db.Model):
    """Booking model linking users to rooms with date ranges."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default="confirmed")
    discount_applied = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Define relationships for easy access to related objects
    user = db.relationship('User', backref='bookings')
    room = db.relationship('Room', backref='bookings')

    def __repr__(self):
        return f"<Booking {self.id}>"
