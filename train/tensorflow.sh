#!/bin/bash
docker run -it -v $PWD/train:/tmp -w /tmp tensorflow/tensorflow:latest-gpu python /tmp/script.py