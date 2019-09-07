from flask import Flask
from flask import request
from flask import Response
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def task1():
    res = request.query_string.decode('utf-8')
    res = res.split('&')
    res = '\n'.join(res)

    return Response(res, mimetype='text/plain')


if __name__ == '__main__':
    app.run('0.0.0.0', port=os.getenv('PORT', '8080'))
