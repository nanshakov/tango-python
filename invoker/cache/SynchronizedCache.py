import threading
import time
from collections import OrderedDict
from datetime import datetime
from multiprocessing import Lock

from invoker.cache.CacheInterface import CacheInterface


class SynchronizedCache(CacheInterface):
    """Thread safe local cache"""
    orderedDict = OrderedDict()
    lock = Lock()

    def __init__(self, ttl_in_sec):
        """Constructor"""
        self.ttl_in_sec = ttl_in_sec
        threading.Thread(target=self.__cleanup, args=(ttl_in_sec,), daemon=True).start()

    def add(self, key, value):
        self.lock.acquire()
        self.orderedDict[key] = [value, self.__current_timestamp_in_ms()]
        self.lock.release()

    def get(self, key):
        value = None
        self.lock.acquire()
        data = self.orderedDict.pop(key, None)
        if data is not None:
            value = data[0]
            # We need update timestamp to up value in order dic to save delete performance
            self.orderedDict[key] = [value, self.__current_timestamp_in_ms()]
        self.lock.release()
        return value

    @staticmethod
    def __current_timestamp_in_ms():
        return int(datetime.now().timestamp() * 1000)

    def __cleanup(self, ttl_in_sec):
        """Delete an old data without full scan"""
        ttl_in_ms = ttl_in_sec * 1000
        while True:
            time.sleep(ttl_in_sec)
            current_ts = self.__current_timestamp_in_ms()
            self.lock.acquire()
            for key, value in self.orderedDict.items():
                if value[1] > current_ts - ttl_in_ms:
                    break
                else:
                    self.orderedDict.pop(key, None)
            self.lock.release()
