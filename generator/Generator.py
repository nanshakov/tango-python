import logging

from flask import Flask

app = Flask(__name__)

logging.basicConfig(
    format=f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    level=logging.DEBUG)


@app.route('/ping')
def ping():
    return '{pong}'


if __name__ == '__main__':
    app.run()
