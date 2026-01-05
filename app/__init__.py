from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from app.auth.routes import auth_bp
    from app.main.routes import main_bp
    from app.posts.routes import posts_bp
    from app.comments.routes import comments_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(posts_bp, url_prefix="/posts")
    app.register_blueprint(comments_bp, url_prefix="/comments")

    with app.app_context():
        db.create_all()

    return app
