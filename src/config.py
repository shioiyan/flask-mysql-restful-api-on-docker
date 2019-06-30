import os


class DevelopmentConfig:

  # SQLAlchemy
  # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(
  #   **{
  #     'user': os.getenv('DB_USER', 'root'),
  #     'password': os.getenv('DB_PASSWORD', 'hoge'),
  #     'host': os.getenv('DB_HOST', 'db'),
  #     'database': os.getenv('DB_DATABASE', 'hoge'),
  #   })

  # SQLAlchemy
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(
    **{
      'user': os.getenv('DB_USER', 'root'),
      'password': os.getenv('DB_PASSWORD', ''),
      'host': os.getenv('DB_HOST', 'docker.for.mac.localhost'),
      'database': os.getenv('DB_DATABASE', 'hoge'),
    })

  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = False

Config = DevelopmentConfig

