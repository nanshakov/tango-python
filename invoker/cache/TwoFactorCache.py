import redis

from cache.CacheInterface import CacheInterface
from cache.SynchronizedCache import SynchronizedCache
from config import RedisConfig
from config import LocalCacheConfig


class TwoFactorCache(CacheInterface):
    """Store data local and in Redis"""

    def __init__(self, redis_config: RedisConfig, local_cache_config: LocalCacheConfig):
        """Constructor"""
        self.cache = SynchronizedCache(local_cache_config.ttl_in_sec)
        self.redis = redis.Redis(
            host=redis_config.host,
            port=redis_config.port,
            password=redis_config.password)

    def add(self, key, value):
        self.cache.add(key, value)
        self.redis.set(key, value)

    def get(self, key):
        value = self.cache.get(key)
        if value is None:
            value = self.redis.get(key)
            if value is not None:
                self.cache.add(key, value)
        return value
