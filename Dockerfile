# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /FDA
COPY requirements.txt /FDA/
RUN pip install -r requirements.txt
COPY . /FDA/