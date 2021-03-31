FROM python:3.7

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN mkdir /app
RUN mkdir /app/images
RUN mkdir /app/documents
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
# downgrade h5py: https://github.com/Shawn-Shan/fawkes/issues/75
RUN pip install --upgrade h5py==2.10.0
COPY . /app

CMD python /app/bot.py