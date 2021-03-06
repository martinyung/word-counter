import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  DEBUG = False
  SCRF_ENABLED = True
  SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
  DEBUG = False

class DevelopmentConfig(Config):
  DEVELOPMENT = True
  DEBUG = True