FROM python:3.11.3-slim

WORKDIR /app

COPY . .

RUN chmod 777 /app && \
  apt-get update && apt-get install -y wget && \
  wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
  apt-get install ./google-chrome-stable_current_amd64.deb -y && \
  pip install -r requirements.txt
