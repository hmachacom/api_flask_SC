import MySQLdb
from os import environ

"""Preprocesamiento de archivo csv para cargar a la base de datos"""
def read_csv(file):
    lines = 0
    file_csv = "movies.csv"
    if file:
        file_csv = file
    try:
        with open(file_csv, mode="r") as csvfile:
            lines = sum(1 for line in csvfile)
        movies_list = []
        with open(file_csv, mode="r") as csvfile:
            csvfile.readline()
            for line in range(lines):
                movie = csvfile.readline().replace("\n", "").split(",")
                if len(movie) == 6:
                    movie[4] = int(movie[4])
                    movie[5] = int(movie[5])
                    movies_list.append(movie)
        return movies_list
    except Exception as error:
        print(f"Error al cargar el archivo: {error}")


def query_mysql_insert(query:str, movie:tuple):
    """ Insert date in data base"""
    try:
        db = MySQLdb.connect(
            host='localhost', port=3306,
            user=environ.get('user'), passwd=environ.get('passwd'),
            db='movies_software_colombia'
        )
        cur = db.cursor()
        cur.execute(query, movie)
        db.commit()
        cur.close()
        db.close()
        return 1
    except Exception as error:
        print(error)
        print("error la conexion a la base de datos")
        return 0

def preload_db(movies_list):
    """ Preload date in data base"""
    for movie in movies_list:
        query_mysql_insert("INSERT INTO movies VALUES(%s, %s, %s, %s, %s, %s);", tuple(movie))

if __name__ == '__main__':
    preload_db(read_csv(None))
