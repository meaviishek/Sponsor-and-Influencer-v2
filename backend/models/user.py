from datetime import datetime
from database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # "admin", "sponsor", "influencer"
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    approved = db.Column(db.Boolean, default=False)

    # Relationships
    logs = db.relationship('UserLog', backref='user', lazy=True)
    sponsor_profile = db.relationship('Sponsor', uselist=False, back_populates='user')
    influencer_profile = db.relationship('Influencer', uselist=False, back_populates='user')
