import MySQLdb

"""Preprocesamiento de archivo csv para cargar a la base de datos"""

lines = 0
file_csv = "../movies.csv"
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
except Exception as error:
    print(f"Error al cargar el archivo: {file_csv}")


def query_mysql_insert(query:str, movie:tuple):
    try:
        db = MySQLdb.connect(
            host='localhost', port=3306,
            user='root', passwd='H2502',
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

def preload_db():
    for movie in movies_list:
        query_mysql_insert("INSERT INTO movies VALUES(%s, %s, %s, %s, %s, %s);", tuple(movie))
