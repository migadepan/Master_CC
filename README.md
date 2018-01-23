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


# Orquestación

La orquestación de las máquinas necesarias para el proyecto, se ha realizado utilizando la herramienta Vagrant, al ser compatible con azure. En el siguiente enlace se pueden seguir los pasos para la instalación y orquestación.

Tanto el sistema operativo como el aprovisionamiento es el utilizado en las versiones anteriores. Podemos ver una guia de instalacion en el [siguiente enlace](https://github.com/migadepan/Master_CC/tree/master/orquestacion)


Despliegue Vagrant:52.232.4.7


# Aprovisionamiento

El aprovisionamiento se ha realizado sobre una máquina virtual de aws con la versión 16.04 de ubuntu utilizando chef-solo por su sencillez. Para mas detalles -> [Readme](https://github.com/migadepan/Master_CC/tree/master/provision/chef-solo)

## Despliegue

Para la automatización se ha utilizado el servicio de virtualización de Azure. Para mas detalles -> [Readme](https://github.com/migadepan/Master_CC/tree/master/automatizacion)

Despliegue:52.224.181.107

## Contenedores

Hemos trabajado con Docker, que es un proyecto de código abierto que automatiza el despliegue de aplicaciones en contenedores, proporcionando una capa de abstracción y automatizando la Virtualización. Ver mas -> [Readme](https://github.com/migadepan/Master_CC/tree/master/contenedores)

Contenedor:https://serviciocc.azurewebsites.net/

Dockerhub:https://hub.docker.com/r/migadepan/master_cc/


## Licencia

Este proyecto será liberado bajo la licencia [GNU GPL V3]

