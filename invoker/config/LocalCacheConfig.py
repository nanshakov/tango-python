import os


class LocalCacheConfig:
    def __init__(self):
        """Constructor"""
        self.ttl_in_sec = os.environ['TTL_IN_SECONDS']
