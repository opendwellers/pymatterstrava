from stravalib.client import Client
from numpy import  array_equal 

import ConfigParser
import time
import requests
import json

#client = Client()
#access_token = client.exchange_code_for_token(client_id=11801, client_secret='f1d4b15369eb1e8f6e7bb39bbaa65942e127577d', code='139090cec37a555b4577c50a38a8114523492c23')

#client.access_token = access_token
#client.access_token = '1d049e3eecd42b4b3f9469922485940401031382'
#athlete = client.get_athlete()
#client.get_activities(
#print("For {id}, I now have an access token ".format(id=athlete.id))

#clubs = athlete.clubs

#print(clubs)


class StravaBot:
    def __init__(self):
        Config = ConfigParser.ConfigParser()
        Config.read("config")
        Config.sections()

        self.clientId = Config.get('Strava', 'ClientId')
        self.clientSecret = Config.get('Strava', 'ClientSecret')
        self.clientAccessToken = Config.get('Strava', 'ClientAccessToken')
        self.clubId = Config.get('Strava', 'ClubId')

        self.mattermostUrl = Config.get('Mattermost', 'URL')
        self.client = Client()
        self.client.access_token = self.clientAccessToken

        self.club = self.client.get_club(self.clubId)

        print('Bot for {club} is here :^)'.format(club=self.clubId))

    def get_club_members(self):
        return self.client.get_club_members(self.clubId) 

    def post_activity(self, activity):
        payload =  {'text': 'This is a test using python requests and mattermost ingoing webhooks'};
        requests.post(self.mattermostUrl, data=json.dumps(payload), verify=False) 


    def run(self):
        members = self.get_club_members()

        for member in members:
            print(member)

        activities = self.client.get_club_activities(self.clubId, limit=20)

        for activity in activities:
            # TODO post activity
            print(activity)
            self.post_activity(activity)
            time.sleep(10)
            activity.done = True

        while(1):
            new_activities = self.client.get_club_activities(self.clubId, limit=20)
            if (not (array_equal(new_activities, activities))):
                print('No changes!')
            else:
                print('New stuff!')
                # TODO post new activities
                activities = new_activities
            time.sleep(2)

