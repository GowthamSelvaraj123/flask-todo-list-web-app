from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions (do not import models/routes yet)
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    # Import models here to avoid circular import
    from app.models import User
    # Import and register blueprints here
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app
