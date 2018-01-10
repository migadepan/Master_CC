# Despliegue de un contenedor de Docker Hub

## Creación de cuenta y vinculación con GitHub

En primer lugar me he creado una cuenta en Docker, y he enlazado mi repositorio de github.

![Crear cuenta](https://user-images.githubusercontent.com/6852023/34749178-4d3611fa-f5a0-11e7-8dca-a4bfa6ab65a8.png)


![Enlazar github](https://user-images.githubusercontent.com/6852023/34749200-60d2b0b0-f5a0-11e7-9435-84099d491552.png)


# Crear documento dockerfile

A continuación pasamos a crar el documento dockerfile. He utilizado una distribución Debian aunque podría ser CentOS o cualquier otra.

# Despliegue de la máquina virtual

Utilizo el siguiente comando para la creación del deployment user set

![deployment-user-set](https://user-images.githubusercontent.com/6852023/34749417-9cf199de-f5a1-11e7-9e5f-e0db06a3de90.png)

Creo un grupo 

![create-group](https://user-images.githubusercontent.com/6852023/34749442-c0e8222c-f5a1-11e7-8b7f-2c5facd73141.png)

Y creo el plan de servicios


![plan](https://user-images.githubusercontent.com/6852023/34749457-daac8004-f5a1-11e7-9663-a4a8dab398c6.png)


Crear el servicio web con la imagen en Docker Hub:

```
curl -L https://www.opscode.com/chef/install.sh | bash
```

az webapp create --resource-group DockerMasterCC --plan MigaMasterCC --name serviciocc --deployment-container-image-name docker pull migadepan/master_cc


Y finalmente el resultado del comando

![captura de pantalla de 2018-01-10 02-14-27](https://user-images.githubusercontent.com/6852023/34751337-43149140-f5ac-11e7-8d77-b39b1ec70655.png)


![captura de pantalla de 2018-01-10 02-15-40](https://user-images.githubusercontent.com/6852023/34751346-57bd84d0-f5ac-11e7-8ffc-513d3e44b8a9.png)





