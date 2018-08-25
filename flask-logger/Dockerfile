FROM python:latest

RUN apt-get update && apt-get -y install \
        apache2-dev \
        apache2

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# separated because this won't install without apache-dev or equivalent
# and we might want to run this another way
RUN pip install mod_wsgi

COPY flask_logger flask_logger
COPY wsgi.py wsgi.py


# mod_wsgi-express start-server --user www-data --group www-data  --log-to-terminal wsgi.py
