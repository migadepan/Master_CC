# Proyecto Cloud Computing

## Descripción del problema

Actualmente existen en el mercado multitud de dispositivos que nos permiten obtener de forma cómoda datos de nuestro rendimiento deportivo y de las condiciones que nos rodean en cada momento. A su vez, se ha detectado una gran carencia de software especializado
para éstos dispositivos, que saque partido de todos los datos que se pueden obtener mientras se realiza una determinada actividad.
Para la correcta evolución del rendimiento de un escalador, es necesario seguir tres pasos: establecer unos objetivos, seguir las rutinas de entrenamiento establecidas y evaluar si se han logrado esos objetivos. Se presenta una gran dificultad al valorar la respuesta en el rendimiento del individuo ante las rutinas realizadas contando solo con las sensaciones personales del escalador y el encadenamiento de proyectos considerados de un determinado grado de dificultad. 

## Solución propuesta

Con el software desarrollado se pretende dar soporte al entrenamiento de los escaladores, con el principal objetivo de poder ofrecer un seguimiento y valoración de los resultados obtenidos por el individuo a lo largo del tiempo durante los entrenamientos o durante la realización de proyectos en roca, rocódromo, competiciones, etc... Para alcanzar esta solución se ha desarrollado un software que necesita que el usuario incluya algunos datos seleccionados de una base de datos. Aquí es donde se presenta el desarrollo de esta parte del proyecto donde se necesita el almacenamiento y obtención de datos por parte del dispositivo móvil.

## Introducción descriptiva del proyecto

El proyecto necesita:

- Servicio de login en Python.
- Almacenamiento de los datos en la base de datos
- Una `API REST` pública
- Servicio `HTTP` que hará uso de la API

## Arquitectura

Se utilizará una arquitectura basada en microservicios.

- La API REST se realizará en Python
- Servicio HTTP proporcionado con `Apache` y `PHP`

# Aprovisionamiento

El aprovisionamiento se ha realizado sobre una máquina virtual de aws con la versión 16.04 de ubuntu utilizando chef-solo por su sencillez. Para comenzar es necesario instalar la aplicación chef-solo utilizando el siguiente comando:

```
curl -L https://www.opscode.com/chef/install.sh | bash
```

Comenzamos creando el sistema de archivos

## Conexión sftp

Para mayor comodidad utilizamos una conexión sftp para subir los archivos a la máquina aws. Se almacenará la carpeta proyecto dentro de cookbooks y se modificará el archivo node.js para que ejecute las recetas correctas


```
sftp -o StrictHostKeyChecking=no -i "ClaveMaquinaMiga.pem" ubuntu@ec2-34-209-122-195.us-west-2.compute.amazonaws.com

```

## Ejecución de chef-solo

A continuación el resultado de la ejecución de la receta

![capt1-proyecto](https://user-images.githubusercontent.com/6852023/32702090-879cf3be-c7e1-11e7-8781-37be685aa5eb.png)

Por último, se ha creado este archivo con la explicación del proceso.

## Ejecución de la receta de un compañero

Para finalizar el hito, se ha probado la receta de TonyESP y ha funcionado correctamente

![capt1-tony](https://user-images.githubusercontent.com/6852023/32702208-acf2edec-c7e3-11e7-9dd0-051505d54a5c.png)


## Licencia

Este proyecto será liberado bajo la licencia [GNU GLP V3]

