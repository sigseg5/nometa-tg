# nometa-tg
This is a Python Telegram bot that provides an opportunity to automatically delete all metadata from photo and apply [Fawkes](https://github.com/Shawn-Shan/fawkes) tool to hide you face from face recognition apps in social networks etc.

## Info
By default, this bot automatically remove all metadata from photos and apply Fawkes at a minimal mode. You can specify Fawkes settings (`FAWKES_MODE`) in `.env` file.<br>
At this release you can send a photo as photo or document.You will get message if tool can't find any faces.<br>
In future release will be implemented settings manager, and may be video processing.<br>
However, you can find full information about Fawkes tool at [GitHub](https://github.com/Shawn-Shan/fawkes), and [this](https://www.shawnshan.com/files/publication/fawkes.pdf) academic paper

## Requirements
* Telegram account
* (Recommended) Installed [Docker](https://www.docker.com/)

## Usage

### Choosing `FAWKES_MODE`
FAWKES_MODE the tradeoff between privacy and perturbation size. Select from a min, low, mid, high. The higher the mode is, the more perturbation will add to the image and provide stronger protection.<br>
Feel free to play with mods and choose that mostly suits you (I prefer `min` or `low`)<br>
In the image below you can see an example of how the Fawkes tool works (photo from the Fawkes GitHub page).
![](http://sandlab.cs.uchicago.edu/fawkes/files/obama.png)

### Run in Docker
* Add TOKEN to .env file. You can get token from [BotFather](https://www.t.me/BotFather) at Telegram
* (Optional) Run `pip freeze > requirements.txt` if you want to add your own dependencies installed by `pip`
* Run `docker build --tag nometa-tg:0.1.0 .` for build image
* (Optional) Run `docker run --env-file .env nometa-tg:0.1.0 env` for check all environment variables for this image
* Run `docker run --env-file .env nometa-tg:0.1.0` to start
Note: Maybe you should add `sudo` before all Docker-assigned commands

### Run locally
Theoretically should work with Python 3.7, can't test it yet.
I can't guaranty that this will be works, please use Docker
* Create `images` and `documents` folder in project folder
* Add `TOKEN` and `FAWKES_MODE` environment variables to your IDE config e.g. PyCharm. You can get token from [BotFather](https://www.t.me/BotFather) at Telegram. For first run you can set `FAWKES_MODE=min`<br> E.g. ENV_VAR: `PYTHONUNBUFFERED=1;TOKEN=1234567890:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx;FAWKES_MODE=min`
* Run `pip install -r requirements.txt` to install dependencies
* Run `bot.py` to start

## Docker control

### Stop container 
* Run `docker stats` to view all running containers
* Run `docker kill <container_id>`

### Remove image
* Run `docker images` to view list of all images
* Run `docker rmi -f <image_id>`

## Contribute
Any ideas or trouble? Please open [issue](https://github.com/sigseg5/nometa-tg/issues) 
or [pull request](https://github.com/sigseg5/nometa-tg/pulls)

## Sponsorship
You may sponsor this project at my [Patreon](https://patreon.com/sigseg5), it will seriously support me :)

## Communicate
Feel free to write me at [Telegram](https://t.me/kirill_nk)

## Security
At the moment, some dependencies cannot be updated to the latest version due to lack of compatibility with the Fawkes tool.