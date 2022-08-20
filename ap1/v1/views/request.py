from flask import jsonify, request, abort, make_response
from views import app_views
from controllers.querys import get_movie_db_id, get_list_movie, validate_db
from models.read_csv import query_mysql_insert, read_csv
from controllers.validate_request import validate_json_post, validate_id_movie



@app_views.route('/movie', methods=['GET'], strict_slashes=False)
def get_movie():
    """ get movie by id """
    validate_db(read_csv('movies.csv'))
    args = request.args
    id_movie = args.get("id")
    if id_movie:
        try:
            movie_list = get_movie_db_id(int(id_movie))
            if movie_list:
                return jsonify(movie_list)
        except:
            return jsonify("Id not valid"), 400


@app_views.route('/movies', methods=['GET'], strict_slashes=False)
def get_movies():
    """ get list movie """
    validate_db(read_csv('movies.csv'))
    args = request.args
    total = args.get("total")
    order = args.get("order")
    
    if total and order:
        try:
            list_movie = get_list_movie(int(total), str(order))
            return jsonify(list_movie)
        except:
            return jsonify("Args no admit"), 400


@app_views.route('/movie', methods=['POST'], strict_slashes=False)
def post_movie():
    """Post new movie in database"""
    validate_db(read_csv('movies.csv'))
    if not request.get_json():
        abort(400, description="Not a JSON")
    new_movie = request.get_json()
    validate_json = validate_json_post(new_movie)
    if validate_json != 'ok':
        abort(400, description=validate_json)
    validate_id = validate_id_movie(new_movie)
    
    if validate_id:
        abort(400, description=validate_id)
    
    print(tuple(new_movie.values()))
    query_mysql_insert("INSERT INTO movies VALUES(%s, %s, %s, %s, %s, %s);", tuple(new_movie.values()))
    return  make_response(jsonify({"message": "La película fue creada con exito"}), 201)
