#!/bin/bash
sudo docker run -it --gpus all -v $PWD/train:/tmp -w /tmp ghcr.io/ttmx/tf-torch-docker:main bash -c "python /tmp/train.py"
echo "Training started"
#sudo docker run -it -v $PWD/train:/tmp -w /tmp --gpus all ghcr.io/ttmx/tf-torch-docker:main python3.9 /tmp/script.py

#docker run -it -v $PWD/train:/tmp -w /tmp tensorflow/tensorflow:latest-gpu python /tmp/script.py
