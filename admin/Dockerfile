FROM python:3.10.0-slim

# install dev dependencies
RUN apt-get update -y && \
    apt-get install -y python3-dev gcc && \
    apt-get update && apt-get -y install netcat && apt-get clean

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/app"
 
COPY . /app
# COPY run.sh .

RUN apt-get clean && \
    apt-get update && \
    apt-get install -y \
    curl \
    vim \
    tmux \
    build-essential \
    libjpeg-dev \
    libpq-dev \
    python-dev  \
    libmariadb-dev-compat && \pip install --upgrade pip && \
    pip install -r requirements.txt


# CMD python3 manage.py runserver 0.0.0.0:8000
RUN chmod +x run.sh
CMD sh run.sh

