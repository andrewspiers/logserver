import flask


app = flask.Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['POST', 'GET'])
def everything(path):
    # get raw data first
    data = flask.request.get_data(as_text=True)
    r = {
        'path': flask.request.full_path,
        'headers': flask.request.headers,
        'args': flask.request.args,
        'json': flask.request.json,
        'cookies': flask.request.cookies,
        'content_length': flask.request.content_length,
        'content_type': flask.request.content_type,
        'data': data,
    }

    print(r)
    return ('200 OK')
