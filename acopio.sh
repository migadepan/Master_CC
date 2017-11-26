#!/bin/bash

# Crear el grupo de recursos
az group create --name CCMiga --location eastus

# Crear la maquina virtual con el grupo de recursos anterior.
ipAddress=$(az vm create -g CCMiga -n remoteAzureMiga --image UbuntuLTS --generate-ssh-keys | jq -r '.publicIpAddress')

echo Se ha creado la siguiente maquina:
echo -name : remoteAzureMiga
echo -ip : $ipAddress
echo -------------------------

# Abrir puertos
az network nsg create --resource-group CCMiga --location eastus --name remoteAzureMigaNSG
az network nsg rule create --resource-group CCMiga --nsg-name remoteAzureMigaNSG --name remoteAzureMigaNSGRule80 --protocol tcp --priority 1000 --destination-port-range 80
az network nsg rule create --resource-group CCMiga --nsg-name remoteAzureMigaNSG --name remoteAzureMigaNSGRule20 --protocol tcp --priority 999 --destination-port-range 20
az network nsg rule create --resource-group CCMiga --nsg-name remoteAzureMigaNSG --name remoteAzureMigaNSGRule22 --protocol tcp --priority 998 --destination-port-range 22

#provision
echo A continuación utilizamos la provisión con chef-solo:
echo https://github.com/migadepan/Master_CC/tree/master/provision/chef-solo

