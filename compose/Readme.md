# Despliegue de un servicio web utilizando DockerCompose

## Servidor 
Para la creación de la API Rest he decidido utilizar el microframework [Flask](http://flask.pocoo.org/), con el que empecé a trabajar en la práctica anterior y ampliar el servicio de la API. Funciona sobre la imagen python:2.7. Y en el archivo requirements se especifican las instalaciones necesarias para el funcionamiento de la API y la base de datos. [Ver Requirements](https://github.com/migadepan/Master_CC/blob/master/requirements.txt)

A continuación veremos las posibles funcionalidades:

Al acceder a la API con:
```
http://migadns.westeurope.cloudapp.azure.com:5000/
```
Simplemente se muestra un mensaje de bienvenida.

![captura1-1](https://user-images.githubusercontent.com/6852023/35707768-5be691f8-07ab-11e8-958f-6c07a41912df.png)

Lo primero que debemos hacer es utilizar el servicio para crear nuestra base de datos y la tabla vias. Si se realiza correctamente nos devolverá un status true
```
http://migadns.westeurope.cloudapp.azure.com:5000/createdb
```
![captura2-1](https://user-images.githubusercontent.com/6852023/35707781-6736c47e-07ab-11e8-9be3-e7740e11a5c1.png)


Ahora, podemos insertar varias vías por defecto utilizando la dirección
```
http://migadns.westeurope.cloudapp.azure.com:5000/insertAll
```
![captura3-1](https://user-images.githubusercontent.com/6852023/35707789-6f1847c6-07ab-11e8-868c-ebfccf764926.png)

O podemos insertar una a una las vías que deseemos almacenar, utilizando la siguiente dirección:
```
http://migadns.westeurope.cloudapp.azure.com:5000/insert?name=sistema%20comercial&grade=8c&place=Cogollos&style=Deportiva
```
![captura4-1](https://user-images.githubusercontent.com/6852023/35707795-781a0c1a-07ab-11e8-82a1-46a068260539.png)

Y por último, podemos mostrar todas las vías en la siguiente dirección
```
http://migadns.westeurope.cloudapp.azure.com:5000/vias
```

![captura5-1](https://user-images.githubusercontent.com/6852023/35707812-870b968a-07ab-11e8-861c-caecaf1ec4ae.png)


Para ver el status, utilizamos la dirección
```
http://migadns.westeurope.cloudapp.azure.com:5000/status
```
![captura7-1](https://user-images.githubusercontent.com/6852023/35707840-a5602088-07ab-11e8-9e96-e7166eaff875.png)

Y para mostrar una vía por su id tenemos la siguiente opción:
```
http://migadns.westeurope.cloudapp.azure.com:5000/via?id=1
```
![captura6-1](https://user-images.githubusercontent.com/6852023/35707825-9151fcc4-07ab-11e8-9f01-e410f412452b.png)

## Almacenamiento de datos

Para la base de datos se ha elegido mysql por ser ya conocida, y la que estoy utilizando en el proyecto completo de la API. Se ha utilizado la imagen mysql:5.7 

## Despliegue en Azure

Para el despliegue de los contenedores en Azure, he creado una máquina virtual que ya tiene Docker y Docker-compose instalados.
```
az group deployment create --resource-group migadepan     --template-uri https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/docker-simple-on-ubuntu/azuredeploy.json
```
Se accede a la máquina por ssh a migadepan@migadns.westeurope.cloudapp.azure.com y se suben los documentos.
Para la ejecución solo tenemos que utilizar el comando
```
sudo docker-compose up
```
![funcionando](https://user-images.githubusercontent.com/6852023/35708524-e17a3a92-07ae-11e8-9c1f-08cb5cab219b.png)