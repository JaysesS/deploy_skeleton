FROM python:3.8.10

WORKDIR /backend
COPY . /backend

RUN python3 -m pip install -r app/requirements.txt
# RUN cd app/
# RUN pwd
# RUN echo ${GUNICORN_INSTANCE}
# RUN gunicorn --workers 4 --threads 4 --bind 127.0.0.1:5000 -m 007 '${GUNICORN_INSTANCE}'