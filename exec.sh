#!/bin/sh

## Remove older superset docker image
docker rmi ocrapi:latest

## Create and run superset docker image
docker build --tag=ocrapi:latest . 

#RUN DEATCHED(-d)
docker run -d -p 5000:5000 ocrapi:latest