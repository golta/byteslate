import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'thisI$immp0sibble334!22@'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	FLASKY_MAIL_SUBJECT_PREFIX = 'WHO KNOWS'
	FLASKY_MAIL_SENDER = 'ME <ME@EXAMPLE.COM>'
	FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') or 'admin'
	CELERY_BROKER_URL = os.environ.get('REDISCLOUD_URL') or 'redis://127.0.0.1:6379'
	CELERY_BROKER_BACKEND = os.environ.get('REDISCLOUD_URL') or 'redis://127.0.0.1:6379'

	@staticmethod
	def init_app(app):
		pass


class DevelopmentConfig(Config):
	DEBUG = True
	MAIL_SERVER = 'smtp.google.mail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'test@gmail.com'
	MAIL_PASSWORD = 'testme'
	CELERY_BROKER_URL = os.environ.get('REDISCLOUD_URL') or 'redis://127.0.0.1:6379'
	CELERY_BROKER_BACKEND = os.environ.get('REDISCLOUD_URL') or 'redis://127.0.0.1:6379'
	SQLALCHEMY_DATABASE_URI = 'mysql://root:qwerty@localhost/byteboard'
	#SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
	#	'sqlite:///' + os.path.join(basedir, 'appdev.db')


class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
}
