from controllers.querys import get_movie_db_id


def validate_json_post(new_movie:dict):
    args_json_movie = {
        'id': int,
        'film': str,
        'genre':str,
        'studio': str,
        'score': int,
        'year': int
        }
    if new_movie.keys() != args_json_movie.keys():
        return "Missing argument for movie"
    for key in args_json_movie.keys():
        if type(new_movie[key]) != args_json_movie[key]:
            return f"Type error argument: {key} "
    return 'ok'


def validate_id_movie(new_movie:dict):
    movie_list = get_movie_db_id(new_movie['id'])
    if movie_list:
        film = movie_list['film']
        return f"Id already exists for film: {film}"
    return False
