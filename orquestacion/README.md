# Orquestación del proyecto Software para asistencia de escaladores en roca y rocódromo

## Arquitectura utilizada
Se van a utilizar dos máquinas virtuales, una para la base de datos y otra para los servidores REST. Se utilizará en ambas el sistema operativo Ubuntu LTS 16.4 principalmente por familiaridad con dicho sistema, ya que a nivel técnico hubiera sido posible utilizar otra distribución como CentOS o Debian sin ningún problema.

## Software a utilizar
He decidido usar la herramienta Vagrant, porque facilita la creación de entornos virtuales, ahorrando especialmente tiempo con la posibilidad de utilizar los box (imagenes) que más nos convengan y también porque no hay muchas alternativas razonables a esta herramienta.

## Descarga e instalación de Vagrant
Realizamos la instalación del plugin con el siguiente comando. Se ha seleccionado la versión 2.0 ya que para utilizar el plugin de azure es necesario una versión superior a la 1.4, la última estable que ofrece.

```
vagrant plugin install vagrant-azure --plugin-version '2.0.0.pre6'
```
Vamos a necesitar hacer login en el cliente de Azure, el cual se instaló en el apartado de automatización, Instalaciones previas [ver enlace](https://github.com/migadepan/Master_CC/tree/master/automatizacion)

Ejecutamos el cliente y nos logeamos, a continuación necesitamos las variables de entorno de la información de nuestra cuenta de azure para escribirlo en el VagrantFile. Obtendemos esos datos con los siguientes comandos

```
az ad sp create-for-rbac
```
Del anterior nos interesa el tenant, appId y password. Y con el siguiente obtenemos el SubscriptionId.
```
az account list --query "[?isDefault].id" -o tsv 
```

## Ejecución de Vagrant
Una vez editado nuestro archivo Vagrantfile, podemos pasar a ejecutarlo con los siguientes comandos:
```
vagrant box add azure https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box --provider azure
vagrant up --no-paralell
```