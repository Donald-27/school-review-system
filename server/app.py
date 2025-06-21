from flask import Flask
from flask_cors import CORS
from server.models import db, migrate
from server.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from server.routes.users import users_bp
    from server.routes.schools import schools_bp
    from server.routes.reviews import reviews_bp

    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(schools_bp, url_prefix="/schools")
    app.register_blueprint(reviews_bp, url_prefix="/reviews")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(port=5555)
