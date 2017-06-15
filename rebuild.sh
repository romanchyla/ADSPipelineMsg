#!/bin/bash

if [ "`docker images adsmsg | grep adsmsg`" = "" ]; then
  docker build -t adsmsg .
  docker run -it --name adsmsg adsmsg
fi

docker rm adsmsg
docker run -v `pwd`:/app --name adsmsg adsmsg make
