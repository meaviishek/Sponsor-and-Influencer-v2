from database import db
from datetime import datetime
class Campaign(db.Model):
    __tablename__ = 'campaigns'

    id = db.Column(db.Integer, primary_key=True)
    sponsor_id = db.Column(db.Integer, db.ForeignKey('sponsors.id'), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    niche = db.Column(db.String(10), nullable=False)  
    goals = db.Column(db.Text, nullable=True)

    
    sponsor = db.relationship('Sponsor', back_populates='campaigns')
    ad_requests = db.relationship('AdRequest', back_populates='campaign')
    reports = db.relationship('Report', back_populates='campaign')