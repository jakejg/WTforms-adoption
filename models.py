from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

default_image = 'https://cdn3.f-cdn.com/ppic/3151051/logo/7139949/cat%20fb.jpg'

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

class Pet(db.Model):

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)    
    age = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def set_image(self):

        return self.photo_url or default_image


