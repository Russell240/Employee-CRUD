from os import environ
import os

import pymysql

# Load environment variables


class Config(object):
    """
    Common configurations
    """
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    db_url = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flahe:password@localhost:3306/employees'
    SQLALCHEMY_BINDS = {
    'Employees':'mysqldb://flahe:''@localhost',}
    SECRET_KEY ='1234$%'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_PEM=''

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

