FROM python:2.7
MAINTAINER Patrick G. <patrick.pollo.guilbert@gmail.com>

ENV version=0.1

WORKDIR /pymatterstrava

ADD https://github.com/patoupatou/pymatterstrava/archive/v${version}.tar.gz .

RUN pip install numpy stravalib \
    && tar xvfz v${version}.tar.gz \
    && rm v${version}.tar.gz \
    && mv pymatterstrava-${version} pymatterstrava

VOLUME pymatterstrava/configuration

ENTRYPOINT ["python", "pymatterstrava/main.py"]
