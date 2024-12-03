from database import db
class Report(db.Model):
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    content = db.Column(db.Text, nullable=False)  # JSON or detailed text description of the report

    # Relationships
    campaign = db.relationship('Campaign', back_populates='reports')