# tg-nometa bot for run it locally, run in Docker directly
This is a Python Telegram bot that provides an opportunity to automatically delete all metadata from photo and apply [fawkes](https://github.com/Shawn-Shan/fawkes) tool to hide you face from face recognition apps in social networks etc.

## Info
By default this bot automatically remove all metadata from photos and apply fawkes at minimal mode. You can specify metadata deletion and fawkes settings in `.env` file. Tis bot doesn't works with albums yet. 

## Requirements
* Telegram account
* (Only for local running) Python 3.7
* (Recommended) Installed [Docker](https://www.docker.com/)

## Usage

### Run locally
* Add `TOKEN` and `MODE` environment variables to you IDE config e.g. PyCharm. You can get token from [BotFather](https://www.t.me/BotFather) at Telegram. For local running you can set `MODE=dev`<br> E.g. ENV_VAR: `PYTHONUNBUFFERED=1;TOKEN=1234567890:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx;MODE=dev`
* Run `pip install -r requirements.txt` to install dependencies
* Run `bot.py` to start

### Run in Docker
* Edit `MAINTAINER` at Dockerfile
* Add TOKEN to .env file. You can get token from [BotFather](https://www.t.me/BotFather) at Telegram
* (Optional) Run `pip freeze > requirements.txt` to add your own dependencies installed by `pip`
* Run `docker build --tag app_name:1.0 .` for build image
* (Optional) Run `docker run --env-file .env app_name:1.0 env` for view all environment variables for this image
* Run `docker run --env-file .env test:1.0` to start

## Docker
### Remove image
* Run `docker images` to view list of all images
* Run `docker rmi -f <image_id>`

### Stop container 
* Run `docker stats` to view all running containers
* Run `docker kill <container_id>`

## Contribute
Any ideas or trouble? Please open [issue](https://github.com/sigseg5/nometa-tg/issues) 
or [pull request](https://github.com/sigseg5/nometa-tg/pulls) 

## Communicate
Feel free to communicate with me at [Telegram](https://t.me/kirill_nk) 