# Despliegue de un servicio web utilizando DockerCompose

## Servidor 
Para la creación de la API Rest he decidido utilizar el microframework [Flask](http://flask.pocoo.org/), con el que empecé a trabajar en la práctica anterior y ampliar el servicio de la API. A continuación veremos las posibles funcionalidades:

Al acceder a la API con:
```
http://localhost:5000
```
Simplemente se muestra un mensaje de bienvenida.

![captura1](https://user-images.githubusercontent.com/6852023/35703983-39d86440-079e-11e8-86cd-76982b067d37.png)

Lo primero que debemos hacer es utilizar el servicio para crear nuestra base de datos y la tabla vias. Si se realiza correctamente nos devolverá un status true
```
http://localhost:5000/createdb
```
![captura2](https://user-images.githubusercontent.com/6852023/35704002-46f16ee2-079e-11e8-87bb-66bf7bcd0b3d.png)


Ahora, podemos insertar varias vías por defecto utilizando la dirección
```
http://localhost:5000/insertAll
```
![captura3](https://user-images.githubusercontent.com/6852023/35704013-5139cfd4-079e-11e8-9626-4912152250d4.png)

O podemos insertar una a una las vías que deseemos almacenar, utilizando la siguiente dirección:
```
http://localhost:5000/insert?name=sistema%20comercial&grade=8c&place=Cogollos&style=Deportiva
```
![captura4](https://user-images.githubusercontent.com/6852023/35704039-6879d5cc-079e-11e8-9eae-09a13023fbf2.png)


Y por último, podemos mostrar todas las vías en la siguiente dirección
```
http://localhost:5000/vias
```

![captura5](https://user-images.githubusercontent.com/6852023/35704059-775916a2-079e-11e8-960e-e0032bcc2572.png)

Para ver el status, utilizamos la dirección
```
http://localhost:5000/status
```

![capturastatusok](https://user-images.githubusercontent.com/6852023/35704083-87e1e7a6-079e-11e8-8063-0b53dfe45fa6.png)

Y para mostrar una vía por su id tenemos la siguiente opción:
```
http://localhost:5000/via?id=2
```

![captura7](https://user-images.githubusercontent.com/6852023/35704117-b00ebd30-079e-11e8-847d-b46e1868e9d2.png)


