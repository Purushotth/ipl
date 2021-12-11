FROM python:3.9

MAINTAINER purush

ENV PYTHONUNBUFFERED 1

RUN mkdir /ipl
WORKDIR /ipl
COPY ./requirements.txt /requirements.txt
# ADD . /learningcourses
RUN pip install -r /requirements.txt
WORKDIR /ipl

# RUN adduser inblr02-28
# USER inblr02-28

