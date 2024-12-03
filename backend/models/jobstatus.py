from database import db
from datetime import datetime

class JobStatus(db.Model):
    __tablename__ = 'job_status'
    id = db.Column(db.Integer, primary_key=True)
    job_type = db.Column(db.String(50), nullable=False)  # "daily_reminder", "monthly_report", "csv_export"
    status = db.Column(db.String(10), default="Pending")  # "Pending", "Completed", "Failed"
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True) 