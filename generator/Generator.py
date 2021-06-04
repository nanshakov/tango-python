import logging
import threading
import time
from random import uniform

import redis as redis
from flask import Flask

from generator.config.RedisConfig import RedisConfig

app = Flask(__name__)

logging.basicConfig(
    format=f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    level=logging.DEBUG)

redis_config = RedisConfig()
redis = redis.Redis(host=redis_config.host, port=redis_config.port)


@app.route('/ping')
def ping():
    return '{pong}'


def send_to_redis(timeout, users):
    while True:
        time.sleep(timeout)
        [redis.set(i, int(uniform(1, 1000000))) for i in users]


if __name__ == '__main__':
    with open('users.txt') as reader:
        threading.Thread(name='send_to_redis', target=send_to_redis, args=(1, reader.readlines()), daemon=True).start()
    app.run()
