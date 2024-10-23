FROM python:3.10-slim-bullseye

ENV PYTHONPATH .

COPY . .

RUN pip install -r requirements.txt

COPY test test
