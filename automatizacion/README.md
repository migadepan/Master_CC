# Provisionamiento en Azure

## Instalaciones previas

```
#Instalación de jq para el despliegue
sudo apt-get install jq

#Instalación de python
sudo apt-get install python

#Instalación de azure client
echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ wheezy main" | \sudo tee /etc/apt/sources.list.d/azure-cli.list

sudo apt-key adv --keyserver packages.microsoft.com --recv-keys 52E16F86FEE04B979B07E28DB02C46DF417A0893
sudo apt-get install apt-transport-https
sudo apt-get update && sudo apt-get install azure-cli
```
## Uso de AZURE CLI
Hacemos login en azure utilizando az login. 
Nos mostrará la siguiente información To sign in, use a web browser to open the page https://aka.ms/devicelogin and enter the code CKLTUYR9Y to authenticate.
Seguimos el enlace e introducimos el codigo para acceder.

## Creación de Script
El siguiente Script automatiza la cración y el aprovisionamiento de la máquina virtual. 

```
#!/bin/bash

# Crear el grupo de recursos
az group create --name GroupMiga --location eastus

# Crear la maquina virtual con el grupo de recursos anterior.
ipAddress=$(az vm create -g GroupMiga -n MVMiga --image UbuntuLTS --generate-ssh-keys | jq -r '.publicIpAddress')

echo Se ha creado la siguiente maquina:
echo -name : MVMiga
echo -ip : $ipAddress
echo -------------------------

# Abrir puertos
az network nsg create --resource-group GroupMiga --location eastus --name remoteAzureMigaNSG
az network nsg rule create --resource-group GroupMiga --nsg-name RAZMigaNSG --name remoteAzureMigaNSGRule80 --protocol tcp --priority 1000 --destination-port-range 80
az network nsg rule create --resource-group GroupMiga --nsg-name RAZMigaNSG --name remoteAzureMigaNSGRule20 --protocol tcp --priority 999 --destination-port-range 20
az network nsg rule create --resource-group GroupMiga --nsg-name RAZMigaNSG --name remoteAzureMigaNSGRule22 --protocol tcp --priority 998 --destination-port-range 22

#provision
echo A continuación utilizamos la provisión con chef-solo:
echo https://github.com/migadepan/Master_CC/tree/master/provision/chef-solo
```
Una vez realizado el script se ejecuta

```
sh acopio.sh
```


