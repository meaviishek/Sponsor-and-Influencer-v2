from celery import shared_task
from models import Influencer, Campaign, Sponsor, AdRequest
from flask_mail import Message
from flask import render_template
from datetime import datetime
import csv


@shared_task
def send_daily_reminders():
  

    influencers = (
        Influencer.query.join(AdRequest)
        .filter(AdRequest.status == "Pending")
        .distinct()
        .all()
    )

    for influencer in influencers:
        if influencer.user.email:  # Check if email exists
            send_email(
                subject="Reminder: Pending Ad Requests",
                recipient=influencer.user.email,
                body=f"Dear {influencer.user.name}, you have pending ad requests. Please log in to check them."
            )



@shared_task
def send_monthly_reports():
  
    sponsors = Sponsor.query.all()
    for sponsor in sponsors:
       
        campaigns = Campaign.query.filter_by(sponsor_id=sponsor.id).all()
    
        report = render_template('monthly_report.html', sponsor=sponsor, campaigns=campaigns)
        if sponsor.user.email:  
            send_email(
                subject="Monthly Activity Report",
                recipient=sponsor.user.email,
                html=report
            )



@shared_task
def export_campaigns_csv(sponsor_id):
  
    sponsor = Sponsor.query.get(sponsor_id)
    if not sponsor:
        return f"No sponsor found with ID {sponsor_id}."

    campaigns = Campaign.query.filter_by(sponsor_id=sponsor.id).all()
    filename = f"{sponsor.user.name}_campaigns_{datetime.utcnow().strftime('%Y%m%d')}.csv"
    filepath = f"/tmp/{filename}"
    
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Description', 'Start Date', 'End Date', 'Budget', 'Visibility', 'Goals']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for campaign in campaigns:
            writer.writerow({
                'Description': campaign.description,
                'Start Date': campaign.start_date.strftime('%Y-%m-%d'),
                'End Date': campaign.end_date.strftime('%Y-%m-%d'),
                'Budget': campaign.budget,
                'Visibility': campaign.visibility,
                'Goals': campaign.goals
            })
    
    if sponsor.user.email: 
        send_email(
            subject="Campaign CSV Export Complete",
            recipient=sponsor.user.email,
            body=f"Your campaigns have been exported to {filename}.",
            html=None
        )



def send_email(subject, recipient, body=None, html=None):
    """
    Helper function to send emails using Flask-Mail.
    """
    from app import mail  
    msg = Message(subject=subject, recipients=[recipient], body=body, html=html)
    mail.send(msg)
