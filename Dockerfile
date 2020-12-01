FROM python:3.7
MAINTAINER <abc@test.com>

RUN pip install --upgrade pip
RUN mkdir /app
RUN mkdir /app/images
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ADD . /app
WORKDIR /app

CMD python /app/bot.py