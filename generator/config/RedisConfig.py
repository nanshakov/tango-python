import os


class RedisConfig:
    def __init__(self):
        """Constructor"""
        self.host = os.getenv('REDIS_HOST', 'localhost')
        self.port = os.getenv('REDIS_PORT', '6379')
