from stravalib.client import Client

import ConfigParser

#client = Client()
#access_token = client.exchange_code_for_token(client_id=11801, client_secret='f1d4b15369eb1e8f6e7bb39bbaa65942e127577d', code='139090cec37a555b4577c50a38a8114523492c23')

#client.access_token = access_token
#client.access_token = '1d049e3eecd42b4b3f9469922485940401031382'
#athlete = client.get_athlete()
#print("For {id}, I now have an access token ".format(id=athlete.id))

#clubs = athlete.clubs

#print(clubs)


class StravaBot:
    def __init__(self):
        Config = ConfigParser.ConfigParser()
        Config.read("config")
        Config.sections()
        print('Bot is here :^)')
        print(Config.sections())

        

