#app factory pattern is used to create the flask application and configure the database.
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

#create database object globally 
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    #configure database
    app.config['SECRET_KEY'] = 'my-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app) #This line initializes the database with the Flask application

    #import the routes from the routes.py file
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    app.register_blueprint(auth_bp) #register the auth blueprint
    app.register_blueprint(tasks_bp) #register the tasks blueprint

    return app