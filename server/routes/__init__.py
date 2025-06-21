from flask import Blueprint
from .users import users_bp
from .schools import schools_bp
from .reviews import reviews_bp

def register_routes(app):
    app.register_blueprint(users_bp)
    app.register_blueprint(schools_bp)
    app.register_blueprint(reviews_bp)
