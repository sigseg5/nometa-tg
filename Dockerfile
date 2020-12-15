FROM python:3.7
MAINTAINER <abc@test.com>

RUN pip install --upgrade pip
RUN mkdir /app
RUN mkdir /app/images
RUN mkdir /app/documents
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
# downgrade h5py: https://github.com/Shawn-Shan/fawkes/issues/75
RUN pip install --upgrade h5py==2.10.0
ADD . /app
WORKDIR /app

CMD python /app/bot.py