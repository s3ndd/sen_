import os

from dotenv import load_dotenv

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(APP_ROOT, '.env')
load_dotenv(env_path)


class BaseConfig(object):
    """
    Base config class. This fields will use by production and development server
    """
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig(BaseConfig):
    """
    Development config class
    """
    DEBUG = True
    TESTING = False
    FLASK_ENV = 'development'


config = {
    'development': 'config.DevelopmentConfig',
}


def configure_app(app):
    """
    Configure app function
    :param app: Flask app
    :return: Flask app
    """
    config_name = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config[config_name])
    return app
