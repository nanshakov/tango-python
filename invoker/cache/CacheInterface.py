class CacheInterface:
    def add(self, key, value):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError
