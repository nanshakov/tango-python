import logging

from flask import Flask, request, jsonify, abort

from cache.TwoFactorCache import TwoFactorCache
from config.LocalCacheConfig import LocalCacheConfig
from config.RedisConfig import RedisConfig

app = Flask(__name__)

logging.basicConfig(
    format=f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    level=logging.DEBUG)

cache = TwoFactorCache(RedisConfig(), LocalCacheConfig())


@app.route('/ping')
def ping():
    return '{pong}'


@app.route('/getinfo')
def getinfo():
    user_id = request.args.get('userId')
    result = cache.get(user_id)
    if result is None:
        abort(404, description="Resource not found")
    return reverse_number(result)


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


def reverse_number(n):
    reversed = 0
    while n != 0:
        r = int(n % 10)
        reversed = reversed * 10 + r
        n = int(n / 10)
    return reversed
