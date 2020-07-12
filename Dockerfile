# Base Image
FROM python:3.5.2-alpine

# Set Workig Directory
WORKDIR /usr/local/app

# Install App Dependencies
RUN pip install --upgrade pip
COPY . .
RUN pip install pipenv
RUN pipenv install
