# api_flask_SC

Esta prueba de programación se deberá implementar utilizando algún framework en Java o
Python que permita crear servicios web tipo REST.

## Como usar
1:
importar la base de datos donde se va ha cargar el archivo csv
	´´movies_software_colombia.sql´´

2:
en la ruta:

´´$ /software_colombia´´

ejecute:

1:

	´´$ pip install -r requirements.txt´´

2:

	´´$ user=user_db passwd=password_db host=localhost  python ap1/v1/app.py´´

Hacer solicitudes

### example:
Solicitudes: 
GET

 http://localhost:8080/movie?id=19

	obtiene:

	´´
	{
	"film": "The Heartbreak Kid",
	"genre": "Comedy",
	"id": 19,
	"score": 41,
	"studio": "Paramount",
	"year": 2007
	}
	´´

http://localhost:8080/movies?total=3&order=desc

	obtiene:

	´´
	[
	{
		"film": "Zack and Miri Make a Porno",
		"genre": "Romance",
		"id": 1,
		"score": 70,
		"studio": "The Weinstein Company",
		"year": 2008
	},
	{
		"film": "Youth in Revolt",
		"genre": "Comedy",
		"id": 2,
		"score": 52,
		"studio": "The Weinstein Company",
		"year": 2010
	},
	{
		"film": "You Will Meet a Tall Dark Stranger",
		"genre": "Comedy",
		"id": 3,
		"score": 35,
		"studio": "Independent",
		"year": 2010
	}
	]
´´

POST

 http://localhost:8080/movies


	´´
	Cuerpo de la petición:
	{
	"id": 78,
	"film":"Van Helsing",
	"genre": "Fantasia",
	"studio": "Universal Studios",
	"score": 100,
	"year": 2004
	}
	Respuesta:
	{
	"message": "La película fue creada con éxito"
	}

	´´