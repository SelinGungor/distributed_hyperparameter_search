FROM python:3.6-stretch

RUN mkdir app

COPY requirements.txt /app

RUN pip install --upgrade -r /app/requirements.txt

COPY . /app

WORKDIR /app/api

ENV FLASK_ENV=development

ENV FLASK_APP=main.py

EXPOSE 5000

CMD python main.py
#CMD flask run --host 0.0.0.0 --port 5000