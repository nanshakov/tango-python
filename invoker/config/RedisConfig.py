import os


class RedisConfig:
    def __init__(self):
        """Constructor"""
        self.host = os.environ['REDIS_HOST']
        self.port = os.environ['REDIS_PORT']
