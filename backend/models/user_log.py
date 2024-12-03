from database import db

class UserLog(db.Model):
    __tablename__ = 'user_logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)
    pending_requests = db.Column(db.Integer, default=0)
    last_reminder_sent = db.Column(db.DateTime, nullable=True)
