# Despliegue de un servicio web utilizando DockerCompose

## Servidor 
Para la creación de la API Rest he decidido utilizar el microframework [Flask](http://flask.pocoo.org/), con el que empecé a trabajar en la práctica anterior y ampliar el servicio de la API. A continuación veremos las posibles funcionalidades:

Al acceder a la API con:
```
http://localhost:5000
```
Simplemente se muestra un mensaje de bienvenida.

------------Poner captura 1

Lo primero que debemos hacer es utilizar el servicio para crear nuestra base de datos y la tabla vias. Si se realiza correctamente nos devolverá un status true
```
http://localhost:5000/createdb
```
----------------------Poner captura 2


Ahora, podemos insertar varias vías por defecto utilizando la dirección
```
http://localhost:5000/insertAll
```
----------------------Poner captura 3

O podemos insertar una a una las vías que deseemos almacenar, utilizando la siguiente dirección:
```
http://localhost:5000/insert?name=sistema%20comercial&grade=8c&place=Cogollos&style=Deportiva
```
--------------------Poner captura 4

Y por último, podemos mostrar todas las vías en la siguiente dirección
```
http://localhost:5000/vias
```
--------------------Poner captura 5

Para ver el status, utilizamos la dirección
```
http://localhost:5000/status
```
--------------------Poner captura 6



