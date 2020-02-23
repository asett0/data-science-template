#!/bin/bash

sudo docker run \
--mount type=volume,src=volume-explore-output,dst=/explore-output/ \
--mount type=volume,src=volume-model-output,dst=/model-output/ \
ds-pipeline

sudo cp -r \
$(sudo docker volume inspect volume-explore-output --format '{{ .Mountpoint }}')/. \
explore-output

sudo cp -r \
$(sudo docker volume inspect volume-model-output --format '{{ .Mountpoint }}')/. \
model-output