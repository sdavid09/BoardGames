# Base Image
FROM python:3.7.8-slim

# Working Directory
WORKDIR /usr/local/app/


RUN pip install --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org

COPY ["./src/Site","./requirements.txt", "./"]

# Install App Dependencies
RUN pip install -r requirements.txt

