# pymatterstrava
Python bot that fetches data from a Strava club and pushes the latest rides to a mattermost channel using incoming webhooks

# TODO

* Add database or cache 
* Make the payload more configurable
* Add docker documentation
* Add an easy way to fetch a token from the Strava api

# Requirements

As the stravalib api is working with python 2.7, I haven't tested this with any other pyenv, so maybe it works with 3+ pyenvs.

`pip install stravalib`

`pip install numpy`

`mv configuration/template_config configuration/config` and complete the variables in configuration/config

You will need to find a way to get a Strava token via oauth as the stravalib provided with pip doesn't provide a way to do so. See the (appropriate documentation)[https://github.com/hozn/stravalib] for more info. As they do not seem to expire, I simply run the url inside postman and analyze the response to get the token once, which I then copy inside the config file.

`python main.py`

# Docker

There's also a quick docker image I made that pulls the code corresponding at the tag and runs it. To configure your bot from outside the container, use the volume specified in the Dockerfile.

# Contributing

At this point when writing this small bot I was new to python and Docker, so the code and standards may not be perfect. If you feel like doing so, you can contribute with pull requests and I'll be glad to help and learn more about Python/Docker this way.
