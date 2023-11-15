from datetime import datetime

from flask import Flask, send_from_directory


app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/datetime')
def current_datetime():
    return datetime.now().isoformat()

@app.route('/<path:path>')
def static_file(path):
    response = send_from_directory('/static', f'{path}.640.jpg')
    response.cache_control.max_age = 3600
    return response

@app.after_request
def add_header(response):
    # 1 hour cache allowed for all responses
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response


if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=True, threaded=True)
