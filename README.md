# pymatterstrava
Python bot that fetches data from a Strava club and pushes the latest rides to a mattermost channel using incoming webhooks

# TODO

* Add database or cache 
* Make the payload more configurable
* Poll every x seconds and post only new activities (different from cache or db)
* Add docker image to quickly run the bot alongside a mattermost instance
* 
# Requirements

As the stravalib api is working with python 2.7, I haven't tested this with any other pyenv, so maybe it works with 3+ pyenvs.

`pip install stravalib`

`pip install numpy`
