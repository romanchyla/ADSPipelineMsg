FROM phusion/baseimage:0.9.17

# Install protobuf.
RUN \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes autoconf automake libtool curl make g++ unzip wget && \
    rm -rf /var/lib/apt/lists/* && \
    wget https://github.com/google/protobuf/releases/download/v3.3.0/protobuf-python-3.3.0.tar.gz && \
    tar -zxvf protobuf-python-3.3.0.tar.gz && \
    cd protobuf-3.3.0/ && \
    ./configure && \
    make -j 2 && \
    make install && \
    ldconfig

RUN \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes python-pip ipython python-dev git && \
    rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip

RUN git clone https://github.com/adsabs/ADSPipelineMsg /app
WORKDIR /app
RUN pip install --ignore-installed six -r requirements.txt

CMD /bin/bash

