from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "User"
    user_id = db.Column(db.String(100),primary_key=True)
    user_name = db.Column(db.String(100))
    language =db.Column(db.String(10))
    picture_url = db.Column(db.String(500))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    address = db.Column(db.String(500))
    create_time= db.Column(db.DateTime, default=datetime.utcnow)
    modify_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id,  user_name,language=None, picture_url=None, longitude=None, latitude=None, address=None) -> None:
        self.user_id = user_id
        self.user_name=user_name
        self.language=language
        self.picture_url=picture_url
        self.longitude=longitude
        self.latitude=latitude
        self.address = address
