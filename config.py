from os import environ
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config(object):
    """
    Common configurations
    """
    SQLALCHEMY_DATABASE_URI =  'mysql://flahe:''@localhost/flaskproject'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

