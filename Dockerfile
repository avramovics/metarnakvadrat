# Stage 1: Build the `pyswisseph` package
FROM python:3.7





# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Install system dependencies
RUN apt-get update && apt-get install -y python3-dev libssl-dev libffi-dev libcurl4-openssl-dev

# Update pip and setuptools
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN pip install urllib3==1.26.7
# Install pyswisseph from PyPI


# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .