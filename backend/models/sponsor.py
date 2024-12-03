from database import db

class Sponsor(db.Model):
    __tablename__ = 'sponsors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    company_name = db.Column(db.String(150), nullable=True)
    industry = db.Column(db.String(50), nullable=True)
    budget = db.Column(db.Integer, nullable=True)

    user = db.relationship('User', back_populates='sponsor_profile')
    campaigns = db.relationship('Campaign', back_populates='sponsor')
