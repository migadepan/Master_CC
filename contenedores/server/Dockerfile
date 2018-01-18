FROM python:3.4-alpine
COPY app.py /home/app.py
COPY requirements.txt /home/requirements.txt
WORKDIR /home
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
