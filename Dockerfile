# syntax=docker/dockerfile:1

FROM python:3.7

COPY . .

RUN pip3 install -r requirements.txt
RUN python -m unittest discover
