from database import db
from datetime import datetime

class AdRequest(db.Model):
    __tablename__ = 'ad_requests'

    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'), nullable=False)
    influencer_id = db.Column(db.Integer, db.ForeignKey('influencers.id'), nullable=False)
    requirements = db.Column(db.Text, nullable=True)
    payment_amount = db.Column(db.Integer, nullable=True)
    by=db.Column(db.Text,nullable=False) 
    status = db.Column(db.String(10), default="Pending")  # "Pending", "Accepted", "Rejected"
    messages = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    campaign = db.relationship('Campaign', back_populates='ad_requests')
    influencer = db.relationship('Influencer', back_populates='ad_requests')
    payment = db.relationship('Payment', uselist=False, back_populates='ad_request')
