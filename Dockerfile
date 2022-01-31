FROM python:3.9

WORKDIR /app

COPY . /app/

ENV DEBUG=1

RUN pip install -r requirements.txt

EXPOSE 8888

CMD gunicorn django_course.wsgi:application --bind 0.0.0.0:8000