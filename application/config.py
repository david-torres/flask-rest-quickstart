class Config(object):
    DEBUG = False
    TESTING = False
    MONGODB_DB = 'businessinsider'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = 'root'
    MONGODB_PASSWORD = ''
    SECRET_KEY = ''


class ProductionConfig(Config):
    MONGODB_DB = ''
    MONGODB_HOST = ''
    MONGODB_PORT = 0
    MONGODB_USERNAME = 'admin'
    MONGODB_PASSWORD = ''
    SECRET_KEY = 'z\x95\x17\xefV>Z\xd5n\xdeb\xa1\xa2\x98\x1a\xd5\xc0\x0b\xfelR\xcf\xbd4'


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'e\xfb\xc8K\xb1\xb9^X\xd9i\xd0;K\xfc)\x86\xa9K\xaf\xed\xfd$q\xd2'


class TestingConfig(Config):
    TESTING = True
