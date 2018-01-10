# Imagen
FROM debian:latest

# Maintener
MAINTAINER Concepcion Carcedo Carnero <conchicarcedo@gmail.com>

#Actualizar e instalar 
RUN apt-get update && apt-get -y install apache2
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*
RUN /usr/sbin/a2dismod 'mpm_*' && /usr/sbin/a2enmod mpm_prefork

RUN apt-get update 
RUN apt-get -y install php php-mysql libapache2-mod-php 
RUN apt-get clean && rm -r /var/lib/apt/lists/*
RUN apt-get install -y python3-pip 

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

RUN /usr/sbin/a2ensite default-ssl
RUN /usr/sbin/a2enmod ssl

# Puertos
EXPOSE 22 
EXPOSE 80 
EXPOSE 443 

# Return status "OK"
RUN rm /var/www/html/index.html
COPY contenedores/index.php /var/www/html/
COPY contenedores/index.php /var/www/html/status/

# Iniciar
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
