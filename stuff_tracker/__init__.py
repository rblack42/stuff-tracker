import os

from flask import Flask

from stuff_tracker.__version__ import get_version


def create_app(test_config=None):
    app = Flask(__name__)

    # Configure the app
    config_type = os.getenv("CONFIG_TYPE", default="config.DevelopmentConfig")
    app.config.from_object(config_type)

    return app


app = create_app()


@app.route("/")
def version():
    return get_version()
