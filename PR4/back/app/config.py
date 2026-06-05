class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://admin:5230@127.0.0.1:5432/dvfu"

class DevelopmentConfig(Config):
    DEBUG = True
