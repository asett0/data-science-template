# syntax=docker/dockerfile:experimental

FROM python:3.7.6-stretch

COPY requirements.txt /

RUN --mount=type=cache,target=/root/.cache/pip pip install -r /requirements.txt

COPY . .
