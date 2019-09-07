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

    r = Response(response=res, mimetype='text/plain', status=200)
    r.headers['Content-Type'] = "text/plain"
    return r


if __name__ == '__main__':
    app.run('0.0.0.0', port=os.getenv('PORT', '8080'))
