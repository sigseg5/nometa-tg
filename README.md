# Python Telegram bot template for run it locally, run in Docker directly or deploy it on Heroku by Heroku Container Registry
This is a Python telegram bot template for run it locally, run in Docker directly or deploy it on Heroku by Heroku Container Registry 

## Requirements
* Telegram account
* (Optional) Installed [Docker](https://www.docker.com/)
* (Optional) Heroku account
* (Optional) Heroku CLI Tool

## Run locally
* Add `TOKEN` and `MODE` environment variables to you IDE config e.g. PyCharm. You can get token from [BotFather](https://www.t.me/BotFather) at Telegram. For local running you can set `MODE=dev`<br> E.g. ENV_VAR: `PYTHONUNBUFFERED=1;TOKEN=1234567890:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx;MODE=dev`
* Run `pip install -r requirements.txt` to install dependencies
* Run `bot.py` to start

## Run in Docker
* Edit `MAINTAINER` at Dockerfile
* (Optional) Specify Python version at Dockerfile
* Add TOKEN to .env file. You can get token from [BotFather](https://www.t.me/BotFather) at Telegram
* (Optional) Run `pip freeze > requirements.txt` to add your own dependencies installed by `pip`
* Run `docker build --tag app_name:1.0 .` for build image
* (Optional) Run `docker run --env-file .env app_name:1.0 env` for view all environment variables for this image
* Run `docker run --env-file .env test:1.0` to start

## Results
After running bot.py using your preferred option, you will get:<br>
`2018–12–14 15:12:21,500 — root — INFO — Starting bot`<br>
If you go to your bot in Telegram and press Start button, you will get:<br>
`2018–12–14 15:12:36,617 — root — INFO — User <user_id> started bot`<br>
And if you type /random command, you will get:<br>
`2018–12–14 15:12:38,238 — root — INFO — User <user_id> randomed number 2`

## Remove image
* Run `docker images` to view list of all images
* Run `docker rmi -f <image_id>`

## Stop container 
* Run `docker stats` to view all running containers
* Run `docker kill <container_id>`

## Deploy on Heroku
Detailed guidance in [this](https://medium.com/python4you/creating-telegram-bot-and-deploying-it-on-heroku-471de1d96554) article

To launch your bot in Heroku you should go through the next steps:
* Create an account or use an existing one
* Create an application (remember about `HEROKU_APP_NAME`)
* Specify environmental variables in Settings tab of your application (`MODE=prod`, `TOKEN` `HEROKU_APP_NAME`)
* Setting env variables.

You can read full instructions about deploying images to Heroku [here](https://devcenter.heroku.com/articles/container-registry-and-runtime).

Go to the directory where you place bot.py, Dockerfile and execute next steps:
* Download Heroku CLI here
* Login
`heroku container:login`

* Build and push an image
`heroku container:push --app <HEROKU_APP_NAME> web`

* Create a new release
`heroku container:release --app <HEROKU_APP_NAME> web`

* Watch logs
`heroku logs --tail --app <HEROKU_APP_NAME>`

After some time, you should be able to see logs of your bot.

## Note
This repository based on this [repo](https://github.com/artemrys/python-telegram-bot-heroku-example) and [article](https://medium.com/python4you/creating-telegram-bot-and-deploying-it-on-heroku-471de1d96554) with some improvements and instructions, big thanks to Artem Rys!
