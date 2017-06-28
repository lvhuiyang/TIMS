FROM python:3.6.1

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD gunicorn -w4 -b0.0.0.0:8000 TIMS.wsgi:application

EXPOSE 8000