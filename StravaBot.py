from stravalib.client import Client
from stravalib.unithelper import kilometers, kilometers_per_hour, meters
from numpy import not_equal

import ConfigParser
import time
import requests 
import json


class StravaBot:
    def __init__(self):
        Config = ConfigParser.ConfigParser()
        Config.read("configuration/config")
        Config.sections()

        self.clientId = Config.get('Strava', 'ClientId')
        self.clientSecret = Config.get('Strava', 'ClientSecret')
        self.clientAccessToken = Config.get('Strava', 'ClientAccessToken')
        self.clubId = Config.get('Strava', 'ClubId') 
        self.mattermostUrl = Config.get('Mattermost', 'URL') 
        self.delay = Config.get('Bot', 'Delay')

        self.client = Client()
        self.client.access_token = self.clientAccessToken

        self.club = self.client.get_club(self.clubId)

        print('Bot for club {name} with id {id} is here :^)'.format(name=self.club.name, id=self.clubId))

    def post_activity(self, activity):
        payload = {}
        if (activity.athlete.firstname is None):
            activity.athlete = self.client.get_athlete(activity.athlete.id)

        payload = {'text': u':bicyclist: *{first_name} {last_name} : distance: {distance}, speed: {speed}, climbing: {climbing}* http://strava.com/activities/{id} {desc} :bicyclist:'.format(first_name=activity.athlete.firstname, last_name=activity.athlete.lastname, distance=kilometers(activity.distance), speed=kilometers_per_hour(activity.average_speed), climbing=meters(activity.total_elevation_gain), id=activity.id, desc=activity.name)}
        print(payload)
        requests.post(self.mattermostUrl, data=json.dumps(payload), verify=False)

    def get_activity_details(self, activity):
        return self.client.get_activity(activity.id)

    def get_new_activities(self, old_activities, new_activities):
        new_list = []
        new_activity_ids = []
        old_activity_ids = []
        for new_activity in new_activities:
            new_activity_ids.append(new_activity.id)
        for old_activity in old_activities:
            old_activity_ids.append(old_activity.id)

        diff_ids = list(set(new_activity_ids) - set(old_activity_ids))
        new_list = [act for act in new_activities if act.id in diff_ids]

        return new_list

    def run(self):

        activities = set(self.client.get_club_activities(self.clubId, limit=3))
        new_activities = activities

        for activity in activities:
            details = self.get_activity_details(activity)
            self.post_activity(details)

        while(1):
            new_activities = set(self.client.get_club_activities(self.clubId, limit=3))
            diff_activities = self.get_new_activities(activities, new_activities)
            if len(diff_activities) > 0:
                print('changes!')
                print(diff_activities)
                for new_activity in diff_activities:
                    details = self.get_activity_details(new_activity)
                    self.post_activity(details)
            else:
                print('no changes')

            activities = new_activities
            time.sleep(float(self.delay))
