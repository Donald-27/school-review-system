from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from server.models import db
from server.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)
    Migrate(app, db)

    from server.routes.users import users_bp
    from server.routes.schools import schools_bp
    from server.routes.reviews import reviews_bp

    app.register_blueprint(users_bp)
    app.register_blueprint(schools_bp)
    app.register_blueprint(reviews_bp)

    return app

app = create_app()
@app.route('/')
def index():
    return {'message': 'Welcome to the School Review API'}


if __name__ == "__main__":
    app.run(port=5555)
