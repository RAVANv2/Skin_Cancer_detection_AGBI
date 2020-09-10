# Base Image 
FROM ubuntu:18.04

# Install packages
RUN apt-get update && apt-get install -y python3 python3-pip sudo 


# Moving my all files to docker
COPY . /app

# Moving to my app folder
RUN cd /app && pip3 install -r requirements.txt

# After install all packages we have to land on our app folder
WORKDIR /app 