#!/bin/bash

sudo docker run \
--mount type=volume,src=volume-explore-output,dst=/explore-output/ \
ds-pipeline

sudo cp -r \
$(sudo docker volume inspect volume-explore-output --format '{{ .Mountpoint }}')/. \
explore-output