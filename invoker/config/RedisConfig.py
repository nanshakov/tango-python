import logging
import os


class RedisConfig:
    def __init__(self):
        """Constructor"""
        self.host = os.getenv('REDIS_HOST', 'localhost')
        self.port = os.getenv('REDIS_PORT', '6379')
        self.password = os.getenv('REDIS_PASS', '')
        logging.debug(f"REDIS_HOST {self.host}")
        logging.debug(f"REDIS_PORT {self.port}")
