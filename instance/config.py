import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'hotel.db')

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///hotel.db"
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
