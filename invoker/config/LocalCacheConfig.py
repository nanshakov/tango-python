import os


class LocalCacheConfig:
    def __init__(self):
        """Constructor"""
        self.ttl_in_sec = os.getenv('TTL_IN_SECONDS', 5)
