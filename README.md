[![Build Status](https://travis-ci.org/adsabs/adsmsg.svg)](https://travis-ci.org/adsabs/adsmsg)
[![Coverage Status](https://coveralls.io/repos/adsabs/adsmsg/badge.svg)](https://coveralls.io/r/adsabs/adsmsg)

# adsmsg

## Short Summary

Message definitions based on [Google Protocol Buffers](https://developers.google.com/protocol-buffers/) to be used by ADS Pipelines.


## Development

To modify message definition, Protocol Buffers compiler should be installed:

```
sudo apt-get install autoconf automake libtool curl make g++ unzip
wget https://github.com/google/protobuf/releases/download/v3.3.0/protobuf-python-3.3.0.tar.gz
tar -zxvf protobuf-python-3.3.0.tar.gz
cd protobuf-3.3.0/
./configure
make
sudo make install
sudo ldconfig # refresh shared library cache.
```

Alternatively, a docker container can be built:

```
docker build -t adsmsg .
docker run -it --name adsmsg adsmsg
```

### Testing

Travis will run tests automatically. You can manually run them in your machine with:

```
py.test
```

## Maintainer(s)

Sergi
