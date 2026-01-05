from flask import render_template
from app.main import main_bp
from app.models import Post

@main_bp.route("/")
def home():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template("main/index.html", posts=posts)
