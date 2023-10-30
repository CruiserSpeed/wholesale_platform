FROM ubuntu:latest

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    pip3 install -r requirements.txt

WORKDIR /app
COPY ./src/ .

CMD python3 run.py