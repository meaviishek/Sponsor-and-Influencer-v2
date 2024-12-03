from database import db

class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    ad_request_id = db.Column(db.Integer, db.ForeignKey('ad_requests.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(10), default="Pending")  # e.g., "Completed", "Failed", "Pending"
    payment_date = db.Column(db.DateTime, default=db.func.now())

    # Relationships
    ad_request = db.relationship('AdRequest', back_populates='payment')