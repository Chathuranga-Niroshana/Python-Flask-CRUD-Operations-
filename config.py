from decouple import config
import os

BASE_DRI = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_TRACK_NOTIFICATIONS = config("SQLALCHEMY_TRACK_NOTIFICATIONS",cast=bool)


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(BASE_DRI,'dev.db')
    DEBUG = True
    SQLALCHEMY_ECHO=True


class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass
