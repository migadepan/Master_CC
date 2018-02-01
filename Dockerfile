FROM python:2.7
LABEL maintainer="Conchi Carcedo"

COPY . /opt/www
WORKDIR /opt/www

RUN pip install -r requirements.txt

EXPOSE 5000
CMD python app.py
