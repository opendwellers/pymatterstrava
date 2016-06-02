from stravalib.client import Client
from numpy import  array_equal 

import ConfigParser
import time
import requests
import json

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

        print('Bot for club {name} with id {id} is here :^)'.format(name=self.club.name, id=self.clubId))

    def get_club_members(self):
        return self.client.get_club_members(self.clubId) 

    def post_activity(self, activity):
        if (activity.athlete.firstname is None):
            activity.athlete = self.client.get_athlete(activity.athlete.id)

        payload =  {'text': '*{first_name} {last_name} : {distance}, {speed}, {climbing}* http://strava.com/activities/{id} {desc}'.format(first_name=activity.athlete.firstname, last_name=activity.athlete.lastname, distance=activity.distance, speed=activity.average_speed, climbing=activity.total_elevation_gain, id=activity.id, desc=activity.name)};
        requests.post(self.mattermostUrl, data=json.dumps(payload), verify=False) 

    def get_activity_details(self, activity):
        return self.client.get_activity(activity.id)

    def run(self):
        members = self.get_club_members()

#        for member in members:
#            print(member)

        activities = self.client.get_club_activities(self.clubId, limit=20)

        for activity in activities:
            details = self.get_activity_details(activity)
            self.post_activity(details)
            activity.done = True
            time.sleep(5)

        while(1):
            new_activities = self.client.get_club_activities(self.clubId, limit=20)
            if (not (array_equal(new_activities, activities))):
                print('No changes!')
            else:
                print('New stuff!')
                # TODO post new activities
                activities = new_activities
            time.sleep(2)

