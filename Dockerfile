FROM python:3.7-slim

ENV WORKDIR=/opt/checkout

RUN mkdir -p $WORKDIR

COPY . $WORKDIR

RUN cd $WORKDIR; pip install -e .

WORKDIR $WORKDIR
CMD nosetests
