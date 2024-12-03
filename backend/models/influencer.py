from database import db

class Influencer(db.Model):
    __tablename__ = 'influencers'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category = db.Column(db.String(50), nullable=True)
    niche = db.Column(db.String(50), nullable=True)
    reach = db.Column(db.Integer, nullable=True)
    followers = db.Column(db.Integer, nullable=True)

    # Relationships
    user = db.relationship('User', back_populates='influencer_profile')
    ad_requests = db.relationship('AdRequest', back_populates='influencer')
