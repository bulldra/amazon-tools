FROM python:3.9.6-slim-buster

ENV TZ=JST-9 PYTHONDONTWRITEBYTECODE=1 PIP_NO_CACHE_DIR=on \
    PIP_DISABLE_PIP_VERSION_CHECK=on

RUN apt-get update -y \
    && apt-get install -y git curl make xz-utils file sudo \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /data
WORKDIR /data
COPY ./requirements.txt ./requirements.txt
RUN pip3 install --upgrade pip \
    && pip3 install -r ./requirements.txt \
    && rm ./requirements.txt

RUN mkdir /data/work \
    && mkdir /data/log
