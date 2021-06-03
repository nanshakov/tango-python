import logging
import time
import unittest

from invoker.cache.SynchronizedCache import SynchronizedCache

logging.basicConfig(
    format=f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    level=logging.DEBUG)


class SynchronizedCacheTestCase(unittest.TestCase):

    def test_insert(self):
        cache = SynchronizedCache(2)
        cache.add(1, 1)
        cache.add(2, 2)
        self.assertEqual(2, cache.get(2))

    def test_get_empty_key(self):
        cache = SynchronizedCache(2)
        self.assertEqual(None, cache.get(2))

    def test_cleanup_case_1(self):
        cache = SynchronizedCache(2)
        cache.add(1, 1)
        time.sleep(1)
        self.assertEqual(1, cache.get(1))

    def test_cleanup_case_2(self):
        cache = SynchronizedCache(2)
        cache.add(1, 1)
        time.sleep(3)
        self.assertEqual(None, cache.get(1))


if __name__ == '__main__':
    unittest.main()
