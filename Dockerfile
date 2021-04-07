FROM python:3.7

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN mkdir /app && mkdir /app/images && mkdir /app/documents

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . /app

CMD python /app/bot.py