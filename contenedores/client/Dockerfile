FROM python:3.4-alpine
COPY client.py /home/client.py
COPY requirementscli.txt /home/requirementscli.txt
WORKDIR /home
RUN pip install -r requirementscli.txt
CMD ["python", "client.py"]


