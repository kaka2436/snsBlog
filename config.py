import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'WUzhao1990'
    SQLALCHEMY_COMMIT_ON_TEAEDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = 'Flask'
    FLASKY_MAIL_SENDER = 'kaka2436@163.com'
    FLASKY_ADMIN = os.environ.get('FLASK_ADMIN')

    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    debug = True
    MAIL_SERVER = "smtp.163.com"
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
    'sqlite:////' + os.path.join(basedir,'data-dev.sqlite')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    'sqlite:////' + os.path.join(basedir , 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:////' + os.path.join(basedir , 'data.sqlite')


config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}
