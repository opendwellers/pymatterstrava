FROM frolvlad/alpine-python2:latest
MAINTAINER Patrick G. <patrick.pollo.guilbert@gmail.com>

ENV version=0.5

WORKDIR /pymatterstrava

ADD https://github.com/patoupatou/pymatterstrava/archive/v${version}.tar.gz .

RUN pip install stravalib urllib3 certifi

RUN tar xvfz v${version}.tar.gz \
    && rm v${version}.tar.gz \
    && mv pymatterstrava-${version} pymatterstrava

VOLUME pymatterstrava/configuration

ENTRYPOINT ["python", "pymatterstrava/main.py"]
