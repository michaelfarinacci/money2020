import flask
import json
from flask import Flask, Response, jsonify, request

app = Flask(__name__, static_url_path='/static')

def resp(data=""):
    """Create response data json"""
    data = {'data': data}
    return json.dumps(data)

@app.route('/')
def index():
    #for thread in THREADS.keys():
    #    if not THREADS[thread].is_alive():
    #        del THREADS[thread]
    return flask.render_template('index.html')

@app.route('/test')
def test():
    data = resp("This is the loyalty server!")
    return Response(response=data, status=200, mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
