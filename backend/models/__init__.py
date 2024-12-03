from .sponsor import Sponsor
from .influencer import Influencer
from .campaign import Campaign
from .ad_request import AdRequest
from .user import User
from .payment import Payment
from .report import Report
from .user_log import UserLog
from .jobstatus import JobStatus
from database import db

# Optionally, you can define an `init_app` function to initialize the models with the app instance.

def init_app(app):
    """Initialize models with the Flask app."""
    db.init_app(app)
    with app.app_context():
        db.create_all()  # Creates tables if they don't exist

# This makes it possible to import models directly from `models`.
__all__ = [
    "Sponsor",
    "Influencer",
    "Campaign",
    "AdRequest",
    "User",
    "Payment",
    "Report",
    "UserLog",
    "JobStatus"
]
