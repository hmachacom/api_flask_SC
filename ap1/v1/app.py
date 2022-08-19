from flask import Flask, render_template, make_response, request
from flask import jsonify
from views import app_views

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
    app.run(host='0.0.0.0', port=5000, debug=True)
