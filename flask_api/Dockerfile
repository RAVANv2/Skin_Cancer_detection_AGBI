# Base Image 
FROM ubuntu:18.04

# Install packages
RUN apt-get update && apt-get install -y python3 python3-pip sudo 


# Moving my all files in ubuntu
COPY . /app

# install txt pakages
RUN cd /app && pip3 install -r requirements.txt

# landing into app dir
WORKDIR /app 
