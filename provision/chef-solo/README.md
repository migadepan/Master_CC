# Hito 2

Comenzamos creando el sistema de archivos

## Conexión sftp

Para mayor comodidad utilizamos una conexión sftp para subir los archivos a la máquina aws. Se almacenará la carpeta proyecto dentro de cookbooks y se modificará el archivo node.js para que ejecute las recetas correctas


```
sftp -o StrictHostKeyChecking=no -i "ClaveMaquinaMiga.pem" ubuntu@ec2-34-209-122-195.us-west-2.compute.amazonaws.com

```
Para comenzar es necesario instalar la aplicación chef-solo utilizando el siguiente comando:

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

