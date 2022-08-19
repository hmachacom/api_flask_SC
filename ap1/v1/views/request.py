from flask import jsonify, request, abort, make_response
from views import app_views
from controller.querys import get_movie_db_id, get_list_movie
from controller.read_csv import query_mysql_insert
from controller.validate_request import validate_json_post, validate_id_movie



@app_views.route('/movie', methods=['GET'], strict_slashes=False)
def get_movie():
    """ get movie by id """
    args = request.args
    id_movie = args.get("id")
    if id_movie:
        movie_list = get_movie_db_id(id_movie)
        if movie_list:
            return movie_list, 200
    total = args.get("total")
    order = args.get("order")
    
    if total and order:
        list_movie = get_list_movie(int(total), order)
        return jsonify(list_movie)
    
    return jsonify("Args no admit"), 400


@app_views.route('/movie', methods=['POST'], strict_slashes=False)
def post_movie():
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
