# config.py
import os


class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments
    SQLALCHEMY_TRACK_MODIFICATIONS = False


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
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
        username=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'],
        hostname=os.environ['DB_HOSTNAME'],
        databasename=os.environ['DB_NAME'],
    )


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
