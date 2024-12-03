from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask import session
from redis import Redis
import json
from tasks import export_campaigns_csv

from database import db
from models.user import User
from models.ad_request import AdRequest
from models.sponsor import Sponsor
from models.influencer import Influencer
from models.campaign import Campaign
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token,
    jwt_required, get_jwt_identity, unset_jwt_cookies
)





main_routes = Blueprint('main_routes', __name__, url_prefix='/api')
redis_client = Redis(host='localhost', port=6379, db=1)

jwt = JWTManager()

@main_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data.get('username')
    name=data.get('name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', '').lower()  
    
    if not username or not email or not password or not role:
        return jsonify({"error": "Missing required fields"}), 400


    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already in use"}), 409

   
    password_hash = generate_password_hash(password)


    new_user = User(
        username=username,
        name=name,
        email=email,
        password_hash=password_hash,
        role=role,
        created_at=datetime.utcnow(),
        approved=False 
    )
    db.session.add(new_user)
    db.session.flush()  

    
    profile = None
    if role == "sponsor":
        company_name = data.get('company_name')
        industry = data.get('industry')
        budget = data.get('budget', 0)

        profile = Sponsor(
            user_id=new_user.id,
            company_name=company_name,
            industry=industry,
            budget=budget
        )
        db.session.add(profile)

    elif role == "influencer":
        category = data.get('category')
        niche = data.get('niche')
        reach = data.get('reach', 0)
        followers = data.get('followers', 0)

        profile = Influencer(
            user_id=new_user.id,
            category=category,
            niche=niche,
            reach=reach,
            followers=followers
        )
        db.session.add(profile)
    elif role == "admin":
        db.session.commit()
        return jsonify({"message":"Admin role is created"}), 201
    else:
        db.session.rollback()
        return jsonify({"error": "Invalid role specified"}), 400

    db.session.commit()

  
    user_data = {
        "id": new_user.id,
        "username": new_user.username,
        "name":new_user.name,
        "email": new_user.email,
        "role": new_user.role,
        "approved": new_user.approved,
        "created_at": new_user.created_at,
        "profile": None 
    }

    if role == "sponsor" and profile:
        user_data["profile"] = {
            "company_name": profile.company_name,
            "industry": profile.industry,
            "budget": profile.budget
        }
    elif role == "influencer" and profile:
        user_data["profile"] = {
            "category": profile.category,
            "niche": profile.niche,
            "reach": profile.reach,
            "followers": profile.followers
        }

    return jsonify(user_data), 201

@main_routes.route('/user/data',methods=['GET'])
@jwt_required()
def get_user_data():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if user.approved:
        if user:
             user_data = {
            "user_id": user.id,
            "username": user.username,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "created_at": user.created_at.isoformat()
            }
        if user.role == "sponsor" and user.sponsor_profile:
             sponsor_profile = user.sponsor_profile
             campaigns = [
                {
                    "id": campaign.id,
                    "name": campaign.name,
                    "description": campaign.description,
                    "start_date": campaign.start_date.isoformat(),
                    "end_date": campaign.end_date.isoformat(),
                    "budget": campaign.budget,
                    "niche": campaign.niche,
                    "goals": campaign.goals,
                    "ad_requests": [
                        {
                            "id": ad_request.id,
                            "influencer_id": ad_request.influencer_id,
                            "status": ad_request.status,
                            "by":ad_request.by,
                            "requirements": ad_request.requirements,
                            "payment_amount": ad_request.payment_amount,
                            "created_at": ad_request.created_at.isoformat(),
                        }
                        for ad_request in campaign.ad_requests
                    ],
                }
                      for campaign in sponsor_profile.campaigns
                 ]
             influencers = [
            {
                "id": influencer.id,
                "name":influencer.user.name,
                "category": influencer.category,
                "niche": influencer.niche,
                "reach": influencer.reach,
                "followers": influencer.followers,
                "user_id": influencer.user_id,
                "approved":influencer.user.approved,
                "user_name": influencer.user.username,
            }
            for influencer in Influencer.query.filter(Influencer.user.has(approved=True)).all()
        ] 

             user_data["profile"] = {
                "id":sponsor_profile.id,
                "company_name": sponsor_profile.company_name,
                "industry": sponsor_profile.industry,
                "budget": sponsor_profile.budget,
                "campaigns": campaigns,
            }
             user_data["all_influencers"] = influencers

        elif user.role == "influencer" and user.influencer_profile:
             influencer_profile = user.influencer_profile
             ad_requests = [
                {
                    "id": ad_request.id,
                    "campaign_id": ad_request.campaign_id,
                    "status": ad_request.status,
                    "sponsor_name":ad_request.campaign.sponsor.user.name,
                    "sponsor_username":ad_request.campaign.sponsor.user.username,
                    "requirements": ad_request.requirements,
                    "payment_amount": ad_request.payment_amount,
                    "messages": ad_request.messages,
                    "by":ad_request.by,
                    "created_at": ad_request.created_at.isoformat(),
                    "campaign_details": {
                        "id": ad_request.campaign.id,
                        "name": ad_request.campaign.name,
                        "start_date": ad_request.campaign.start_date.isoformat(),
                        "end_date": ad_request.campaign.end_date.isoformat(),
                        "budget": ad_request.campaign.budget,
                        "niche": ad_request.campaign.niche,
                    } if ad_request.campaign else None,
                }
                for ad_request in influencer_profile.ad_requests
            ]
             campaigns = [
            {
                "id": campaign.id,
                "name": campaign.name,
                "description": campaign.description,
                "start_date": campaign.start_date.isoformat(),
                "end_date": campaign.end_date.isoformat(),
                "budget": campaign.budget,
                "niche": campaign.niche,
                "goals": campaign.goals,
                "sponsor": {
                    "id": campaign.sponsor_id,
                    "name": campaign.sponsor.company_name if campaign.sponsor else None,
                },
            }
            for campaign in Campaign.query.all()
        ]
             user_data["profile"] = {
                "category": influencer_profile.category,
                "niche": influencer_profile.niche,
                "reach": influencer_profile.reach,
                "followers": influencer_profile.followers,
                "ad_requests": ad_requests,
            }
             user_data["all_campaigns"] = campaigns
        elif user.role == "admin":
            all_campaigns = [
            {
                "id": campaign.id,
                "name": campaign.name,
                "description": campaign.description,
                "start_date": campaign.start_date.isoformat(),
                "end_date": campaign.end_date.isoformat(),
                "budget": campaign.budget,
                "niche": campaign.niche,
                "goals": campaign.goals,
                "sponsor": {
                    "id": campaign.sponsor.user.id,
                    "name": campaign.sponsor.user.name,
                    "username": campaign.sponsor.user.username,
                } if campaign.sponsor else None,
            }
            for campaign in Campaign.query.all()
        ]

            all_influencers = [
            {
                "id": influencer.id,
                "name": influencer.user.name,
                "category": influencer.category,
                "niche": influencer.niche,
                "reach": influencer.reach,
                "followers": influencer.followers,
                "user_id": influencer.user_id,
                "username": influencer.user.username,
                "approved":influencer.user.approved
            }
            for influencer in Influencer.query.all()
        ]

            all_ad_requests = [
            {
                "id": ad_request.id,
                "campaign_id": ad_request.campaign_id,
                "influencer_id": ad_request.influencer_id,
                "status": ad_request.status,
                "requirements": ad_request.requirements,
                "payment_amount": ad_request.payment_amount,
                "messages": ad_request.messages,
                "created_at": ad_request.created_at.isoformat(),
                "campaign_name": ad_request.campaign.name if ad_request.campaign else None,
                "influencer_name": ad_request.influencer.user.name,
            }
            for ad_request in AdRequest.query.all()
        ]
            all_sponsors = [
            {
                "id": sponsor.id,
                "name": sponsor.user.name,
                "username": sponsor.user.username,
                "company_name": sponsor.company_name,
                "industry": sponsor.industry,
                "budget": sponsor.budget,
                "user_id":sponsor.user.id,
                "approved": sponsor.user.approved
            }
            for sponsor in Sponsor.query.all()
        ]
        
            user_data["all_sponsors"]=all_sponsors
            user_data["all_campaigns"] = all_campaigns
            user_data["all_influencers"] = all_influencers
            user_data["all_ad_requests"] = all_ad_requests
    
        redis_client.setex(f"user:{user.id}", 3600, json.dumps(user_data))

        return jsonify({"message": "Login successful", "user": user_data}), 200
    else:
        return jsonify({"message": "Your are not approved or flagged"}), 401


# User login
@main_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    if not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid password"}), 401

    if not user.approved:
        return jsonify({"error": "Account awaiting approval"}), 403

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    # user_data = {
    #         "id": user.id,
    #         "username": user.username,
    #         "name": user.name,
    #         "email": user.email,
    #         "role": user.role,
    #         "approved": user.approved,
    #         "created_at": user.created_at.isoformat()
    #         }

    return jsonify({"message": "Login successful","access_token": access_token,
        "refresh_token": refresh_token}), 200



#logout route
@main_routes.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    
    response = jsonify({"message": "Logout successful"})
    unset_jwt_cookies(response)
    return response

@main_routes.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)


def refresh():
    user_id = get_jwt_identity()
    new_access_token = create_access_token(identity=user_id)
    return jsonify({"access_token": new_access_token}), 200



#create campaign
@main_routes.route('/createcampaign', methods=['POST'])
def create_campaign():
    
    data = request.json
    try:
        # Validate required fields
        if not all(key in data for key in ['sponsor_id', 'name', 'start_date', 'end_date', 'budget', 'niche']):
            return jsonify({'error': 'Missing required fields'}), 400

        campaign = Campaign(
            sponsor_id=data['sponsor_id'],
            name=data['name'],
            description=data.get('description'),
            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d'),
            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d'),
            budget=data['budget'],
            niche=data['niche'],
            
        )
        db.session.add(campaign)
        db.session.commit()
        return jsonify({'message': 'Campaign created successfully', 'campaign': campaign.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_routes.route('/delcampaign/<int:campaign_id>',methods=['DELETE'])
def delete_campaign(campaign_id):
    
    try:
        campaign = Campaign.query.get(campaign_id)
        if campaign is None:
            return jsonify({'error': 'Campaign not found'}), 404
        db.session.delete(campaign)
        db.session.commit()
        return jsonify({'message': 'Campaign deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

        
    

@main_routes.route('/editcampaign/<int:campaign_id>', methods=['PUT'])
def update_campaign(campaign_id):
  
    data = request.json
    try:
        campaign = Campaign.query.get(campaign_id)
        if not campaign:
            return jsonify({'error': 'Campaign not found'}), 404

        # Update fields if present in the request
        campaign.name = data.get('name', campaign.name)
        campaign.description = data.get('description', campaign.description)
        campaign.start_date = datetime.strptime(data['start_date'], '%Y-%m-%d') if 'start_date' in data else campaign.start_date
        campaign.end_date = datetime.strptime(data['end_date'], '%Y-%m-%d') if 'end_date' in data else campaign.end_date
        campaign.budget = data.get('budget', campaign.budget)
        campaign.niche = data.get('niche', campaign.niche)
        campaign.goals = data.get('goals', campaign.goals)

        db.session.commit()
        return jsonify({'message': 'Campaign updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500



#influencerRoutes

@main_routes.route('/adr_inf',methods=['POST'])
def ad_request_by_inf():
    try:
        
        data = request.json
        influencer_id = data.get('influencer_id')
        campaign_id = data.get('campaign_id')
       
        payment_amount = data.get('payment_amount')
        by = data.get('by')  
       
        if not influencer_id or not campaign_id:
            return jsonify({'error': 'Influencer ID and Campaign ID are required'}), 400
        
        
        # influencer = Influencer.query.filter_by(user_id=influencer_id).first()
        influencer = Influencer.query.get(influencer_id)
        if not influencer:
            return jsonify({'error': 'Influencer not found'}), 404
        
        influencer_id=influencer.id
        
        campaign = Campaign.query.get(campaign_id)
        if not campaign:
            return jsonify({'error': 'Campaign not found'}), 404

       
        ad_request = AdRequest(
            influencer_id=influencer_id,
            campaign_id=campaign_id,
            payment_amount=payment_amount,
            by=by,
        )
        db.session.add(ad_request)
        db.session.commit()

        return jsonify({'message': 'Ad request created successfully', 'ad_request_id': ad_request.id}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@main_routes.route('/inf/profile',methods=['POST'])
@jwt_required()
def influencer_profile():
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        influencer_profile = Influencer.query.filter_by(user_id=user.id).first()

        data = request.get_json()
        name = data.get('name')
        category = data.get('category')
        reach = data.get('reach')
        followers = data.get('followers')
        if not all([name, category, reach, followers]):
            return jsonify({"error": "All fields are required"}), 400
        if not isinstance(reach, int) or not isinstance(followers, int):
            return jsonify({"error": "Reach and Followers must be integers"}), 400

    
        user.name = name
        influencer_profile.category = category
        influencer_profile.reach = reach
        influencer_profile.followers = followers
    
        db.session.commit()
        return jsonify({
            "message": "Profile updated successfully",
           
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

        

@main_routes.route('/adr_infdel/<int:influencer_id>/<int:campaign_id>', methods=['DELETE'])
def delete_ad_request(influencer_id, campaign_id):
    influencer = Influencer.query.filter_by(user_id=influencer_id).first()
        # influencer = Influencer.query.get(influencer_id)
    if not influencer:
        return jsonify({'error': 'Influencer not found'}), 404
        
    influencer_id=influencer.id
    ad_request = AdRequest.query.filter_by(influencer_id=influencer_id, campaign_id=campaign_id).first()
    if not ad_request:
        return jsonify({'error': 'Request not found'}), 404
    
    db.session.delete(ad_request)
    db.session.commit()
    return jsonify({'message': 'Request canceled successfully'}), 200


# @main_routes.route('/adr_infch/<int:influencer_id>/<int:campaign_id>', methods=['GET'])
# def check_ad_request(influencer_id, campaign_id):
#     influencer = Influencer.query.filter_by(user_id=influencer_id).first()
#         # influencer = Influencer.query.get(influencer_id)
#     if not influencer:
#         return jsonify({'error': 'Influencer not found'}), 404
        
#     influencer_id=influencer.id
       
#     ad_request = AdRequest.query.filter_by(influencer_id=influencer_id, campaign_id=campaign_id).first()
#     exists = ad_request is not None
#     return jsonify({'exists': exists})


@main_routes.route('/ad_request/<int:ad_request_id>/accept', methods=['POST'])
def accept_ad_request(ad_request_id):
    data = request.get_json()
    # requested_by = data.get('by')

    ad_request = AdRequest.query.get(ad_request_id)
    if not ad_request:
        return jsonify({"error": "AdRequest not found"}), 404


    # if ad_request.by != requested_by:
    #     return jsonify({"error": "Permission denied"}), 403


    ad_request.status = "Accepted"
    ad_request.messages = data.get('message', '')
    db.session.commit()

    return jsonify({
        "message": f"AdRequest {ad_request_id} has been accepted.",
        "status": ad_request.status
    }), 200



@main_routes.route('/ad_request/<int:ad_request_id>/reject', methods=['POST'])
def reject_ad_request(ad_request_id):
    data = request.get_json()
    # requested_by = data.get('by')

    ad_request = AdRequest.query.get(ad_request_id)
    if not ad_request:
        return jsonify({"error": "AdRequest not found"}), 404

    # if ad_request.by != requested_by:
    #     return jsonify({"error": "Permission denied"}), 403

    # Update status to "Rejected"
    ad_request.status = "Rejected"
    ad_request.messages = data.get('message', '')
    db.session.commit()

    return jsonify({
        "message": f"AdRequest {ad_request_id} has been rejected.",
        "status": ad_request.status
    }), 200
    


@main_routes.route('/users/<int:user_id>/flag', methods=['POST'])
def flag_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        user.approved = not user.approved
        db.session.commit()

        return jsonify({'message': f"User {'unflagged' if user.approved else 'flagged'} successfully"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        db.session.delete(user)
        db.session.commit()

        return jsonify({'message': 'User deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@main_routes.route('/export_csv', methods=['POST'])
def export_csv():
    sponsor_id = request.json.get('sponsor_id')
    task = export_campaigns_csv.delay(sponsor_id)
    return jsonify({"task_id": task.id, "status": "Processing"}), 202