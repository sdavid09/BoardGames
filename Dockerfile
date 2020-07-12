# Base Image
FROM python:3.5.2-alpine

# Working Directory
WORKDIR /usr/local/app/

# Install App Dependencies
RUN pip install --upgrade pip

COPY ["./src/Site","./requirements.txt", "./"]

RUN pip install -r requirements.txt

