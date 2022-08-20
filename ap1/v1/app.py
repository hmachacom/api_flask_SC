from flask import Flask, render_template, make_response, request
from flask import jsonify
from views import app_views
from controllers.querys import validate_db
from models.read_csv import read_csv
from os import environ

app = Flask(__name__)
app.register_blueprint(app_views)


@app.route('/', methods=['GET'])
def get_id():
    """ root """
    return jsonify({"page": 'ok'})


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == '__main__':
    host = environ.get('host')
    if not host:
        host = '0.0.0.0'
    port = environ.get('port')
    if not port:
        port = 8080
    debug = environ.get('debug')
    if not debug:
        debug = False
    #validate_db(read_csv('software_colombia/ap1/v1/movies.csv'))
    app.run(host, port, debug)
