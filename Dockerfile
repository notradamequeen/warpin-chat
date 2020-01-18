# first stage build
FROM python:3.7 AS base
# copy requirements
COPY requirements.txt .
# install requirements
RUN pip install -r ./requirements.txt
# create web dir
WORKDIR /web
# copy everything to web dir
COPY . /web
