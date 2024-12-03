
from flask import Flask,jsonify
from flask_session import Session 
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager
)
import redis

from config import Config
from database import db, bcrypt, jwt  
from routes.main_routes import main_routes  
from celery_app import make_celery

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

app.config.from_object(Config)  
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_KEY_PREFIX'] = 'session:'

app.config['SESSION_REDIS']=redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=False)



db.init_app(app)  # Initialize the SQLAlchemy instance with the Flask app
bcrypt.init_app(app)  # Initialize bcrypt with the Flask app
jwt.init_app(app)  #
Session(app) 

app.register_blueprint(main_routes)


app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = False
app.config['JWT_SECRET_KEY'] = 'fgfgfgrtryr458@#@#@$#$#'  # Use a strong, secret key
jwt = JWTManager(app)

celery = make_celery(app)
@app.route('/')
def home():
   
    return jsonify(message="Success! You have reached the home page.")

with app.app_context():
    db.create_all()

# Entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
