import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY_BLOG')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = '[SCG]'
    MAIL_SENDER = 'Sinan Can Gulan <sinancangulan@gmail.com>'
    ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = os.environ.get('scg_dbase')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    #fetch dev dbase

class TestingConfig(Config):
    TESTING = True
    #fetch test dbase

class ProductionConfig(Config):
    #fetch production dbase
    SQLALCHEMY_DATABASE_URI = 'mysql:///'

config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
}
