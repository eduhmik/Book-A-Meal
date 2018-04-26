class Config(object):
    """
    Basic app configuration
    """
    DEBUG = False
    
class DevelopmentConfig(Config):
    """Development configs"""
    DEBUG = True


class TestingConfig(Config):
    """Testing configs"""
    TESTING = True
    DEBUG = True

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}

