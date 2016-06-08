FROM python:2.7
MAINTAINER Patrick G. <patrick.pollo.guilbert@gmail.com>

ENV HTTP_PROXY www-proxy.lmc.ericsson.se:8080
ENV HTTPS_PROXY www-proxy.lmc.ericsson.se:8080

RUN mkdir /home/pymatterstrava
WORKDIR /home/pymatterstravao

RUN pip install numpy stravalib

RUN git clone https://github.com/patoupatou/pymatterstrava

VOLUME /home/pymatterstrava/pymatterstrava/configuration

ENTRYPOINT ["python", "/home/pymatterstrava/pymatterstrava/main.py"]
