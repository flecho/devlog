FROM python:2.7
MAINTAINER Joonsang Jo <needoptimism@gmail.com>

ENV INSTALL_PATH /devlog
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY . .
RUN pip install -r requirements.txt

CMD gunicorn "devlog.app:create_app()" -b 0.0.0.0:8000 --access-logfile -
