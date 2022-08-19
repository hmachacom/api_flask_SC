import MySQLdb
from controller.read_csv import preload_db


def connect():
    db = MySQLdb.connect(
            host='localhost', port=3306,
            user='root', passwd='H2502',
            db='movies_software_colombia'
        )
    return db


def disconet(db, cur):
    cur.close()
    db.close()


def validate_db():
    db = connect()
    cur = db.cursor()
    cur.execute('SELECT * FROM `movies`;')
    if cur.rowcount == 0:
        preload_db()
    disconet(db, cur)
    

def get_movie_db_id(id_movie:int):
    db = connect()
    cur = db.cursor()
    cur.execute(f'SELECT * FROM `movies` WHERE `id` = {id_movie}')
    record = cur.fetchall()
    if len(record) > 0 and len(record[0]) == 6:
        movie_list = record[0]
        movie_json = {
            'id': movie_list[0],
            'film': movie_list[1],
            'genre': movie_list[2],
            'studio': movie_list[3],
            'score': movie_list[4],
            'year': movie_list[5],

        }
        return movie_json
    return None


def get_list_movie(total:int, order:str):
    db = connect()
    cur = db.cursor()
    cur.execute(f'SELECT * FROM `movies` ORDER BY `film` {order} LIMIT {total}')
    records = cur.fetchall()
    list_movie = []
    if len(records) == total:
        for record in records:
            if len(record) == 6:
                movie_json = {
                    'id': record[0],
                    'film': record[1],
                    'genre': record[2],
                    'studio': record[3],
                    'score': record[4],
                    'year': record[5],
                }
                list_movie.append(movie_json)
    return list_movie
