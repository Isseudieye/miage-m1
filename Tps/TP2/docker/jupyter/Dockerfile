FROM python:3.13-slim

# set language and time zone
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8


WORKDIR _notebooks


COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt && \
    rm requirements.txt
