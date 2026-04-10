# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime, timezone

""" You will use the empty models.py file that
was provided with your starter code and create a Movie class with the following
columns in your database:
• id (integer)
• title (string)
• description (text)
• poster (string)
• created_at (date time)"""


class Movie(db.Model):

    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100),nullable=False)
    description = db.Column(db.Text(),nullable=False)

    poster = db.Column(db.String(100),nullable=False)
    created_at = db.Column(db.DateTime(),default=lambda: datetime.now(timezone.utc))
