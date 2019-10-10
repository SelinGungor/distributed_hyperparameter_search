FROM python:3.6-stretch

RUN mkdir mnist

COPY requirements.txt /mnist

RUN pip install --upgrade -r /mnist/requirements.txt

COPY . /mnist

WORKDIR /mnist

CMD python mnist/main.py