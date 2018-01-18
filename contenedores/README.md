# Despliegue de un servicio web utilizando DockerCompose
(Cliente en desarrollo)

## Servidor 
Para ello primero vamos a crear el servicio Servidor, he decidido utilizar el microframework [Flask](http://flask.pocoo.org/) he desarrollado un servicio sencillo que devolverá todos los nombres de las vías de escalada o solo uno según su id. Se puede ver en el siguiente [archivo](https://github.com/migadepan/Master_CC/blob/master/contenedores/server/app.py)

## Cliente
(En desarrollo) Aunque el cliente no está terminado podemos ver una muestra del funcionamiento de la herramienta Docker Compose para lanzar dos contenedores con el archivo [docker-compose](https://github.com/migadepan/Master_CC/blob/master/contenedores/docker-compose.yml) que explicaré al final.

## Dockerfiles
Tanto el cliente como el servidor tienen su propio archivo Dockerfile, [aquí el del servidor](https://github.com/migadepan/Master_CC/blob/master/contenedores/server/Dockerfile) donde se especifica la imagen a utilizar, en este caso he seleccionado alpine por ser muy ligera, adecuada para un pequeño servicio web. Con el comando COPY se mueven los archivos al directorio de trabajo del contenedor. También tenemos el archivo requirements.txt que simplemente contiene las dependencias que se instalarán para que todo funcione correctamente. Se ejecuta con RUN y por último CMD indica qué se va a ejecutar al lanzar el contenedor, en éste caso app.py

## Creación de docker-compose
Se especifican los servicios que se van a lanzar y sus dependencias, se lanzará con el comando 

```
sudo docker-compose up
```


![captura de pantalla de 2018-01-18 19-27-58](https://user-images.githubusercontent.com/6852023/35116347-6807a4f2-fc8b-11e7-8627-573eae4cdd88.png)
