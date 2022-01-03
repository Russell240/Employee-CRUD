from os import environ
from dotenv import load_dotenv
import mysql.connector

# Load environment variables
load_dotenv()

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
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://flahe:password@127.0.0.1:3306/employees"
    SQLALCHEMY_BINDS = {
    'Employees':'mysqldb://flahe:''@localhost',}
    SECRET_KEY ='1234$%'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

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

