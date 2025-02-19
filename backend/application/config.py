import os

class Config:
    """Base config."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")
    ##set API key as environment variable and access here

class DevelopmentConfig(Config):
    """Development environment config."""
    DEBUG = True

class ProductionConfig(Config):
    """Production environment config."""
    DEBUG = False

# Default config
config = DevelopmentConfig  # Change this for production
