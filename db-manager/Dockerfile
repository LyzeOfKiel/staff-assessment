FROM python:3.7-buster

RUN pip3 install pymongo

COPY ./db.py .

RUN python db.py
