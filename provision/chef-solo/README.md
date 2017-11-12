# Hito 2

Comenzamos creando el sistema de archivos

## Conexión sftp

Para mayor comodidad utilizamos una conexión sftp para subir los archivos a la máquina aws.


```
sftp -o StrictHostKeyChecking=no -i "ClaveMaquinaMiga.pem" ubuntu@ec2-34-209-122-195.us-west-2.compute.amazonaws.com

```

## Ejecución de chef-solo

A continuación el resultado de la ejecución de la receta

![capt1-hito2](https://user-images.githubusercontent.com/6852023/32699483-e379ee88-c7b6-11e7-866e-31e79d355ab4.png)

Por último, se ha creado este archivo con la explicación del proceso.
