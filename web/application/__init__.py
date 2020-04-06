from flask import Flask, g, current_app
from flask_cors import CORS
from .db_init import get_db


def create_app(config=None):
    app = Flask(__name__)
    # TODO Potential CSRF vulnerability
    # should be removed on production server
    # use for development only
    CORS(app)
    app.config.from_mapping(
        TEMPLATES_AUTO_RELOAD=True,
    )
    #

    with app.app_context():
        get_db().drop_db()
        get_db().generator()

    # Register all blueprints to the app
    from application.views import auth, \
        get_methods, set_methods

    app.register_blueprint(auth.bp, url_prefix='/api')
    app.register_blueprint(get_methods.bp, url_prefix='/api')
    app.register_blueprint(set_methods.bp, url_prefix='/api')

    return app
