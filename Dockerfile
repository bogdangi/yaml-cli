FROM python:alpine3.8

COPY requirements.txt requirements.txt 

RUN pip install -r requirements.txt

COPY main.py /bin/yaml
