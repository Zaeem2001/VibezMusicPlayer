import json
import requests
from SpotifyRefresh import Refresh

class Spotify:

    # initialize our class variables
    def __init__(self):
        self.user_id = "zaeemghauri"  # my Spotify user ID
        self.spotify_token = ""       # the access token, new one will be generated by call_refresh()
        self.device_id = ""           # id of device spotify will play on

        self.angry_list = "spotify:playlist:37i9dQZF1DWXNFSTtym834"          # id for angry emotion playlist
        self.happy_list = "spotify:playlist:37i9dQZF1DWXT8uSSn6PRy"          # id for happy emotion playlist
        self.neutral_list = "spotify:playlist:37i9dQZF1DWWEJlAGA9gs0"        # id for neutral emotion playlist
        self.sad_list = "spotify:playlist:37i9dQZF1DX7gIoKXt0gmx"            # id for sad emotion playlist
        self.surprise_list = "spotify:playlist:37i9dQZEVXcLwZK5DvMjT9"       # id for surprise emotion playlist

    def get_device_id(self):
        # print ("Getting user's device ID")

        query = "https://api.spotify.com/v1/me/player/devices"

        response = requests.get(query, headers={"Content-Type": "application/json",
                                                "Authorization": "Bearer {}".format(self.spotify_token)})
        response_json = response.json()

        self.device_id = response_json["devices"][0]["id"]

    def play_angry(self):
        # print ("Playing angry music >:(")

        query = "https://api.spotify.com/v1/me/player/play?{}".format(self.device_id)
        data = json.dumps({"context_uri": self.angry_list,
                           "offset": {"position": 0},
                           "position_ms": 0})

        response = requests.put(query, data, headers={"Content-Type": "application/json",
                                                      "Authorization": "Bearer {}".format(self.spotify_token)})

    def play_happy(self):
        # print ("Playing happy music :)")

        query = "https://api.spotify.com/v1/me/player/play?{}".format(self.device_id)
        data = json.dumps({"context_uri": self.happy_list,
                           "offset": {"position": 0},
                           "position_ms": 0})

        response = requests.put(query, data, headers={"Content-Type": "application/json",
                                                      "Authorization": "Bearer {}".format(self.spotify_token)})

    def play_neutral(self):
        # print ("Playing neutral music :|")

        query = "https://api.spotify.com/v1/me/player/play?{}".format(self.device_id)
        data = json.dumps({"context_uri": self.neutral_list,
                           "offset": {"position": 0},
                           "position_ms": 0})

        response = requests.put(query, data, headers={"Content-Type": "application/json",
                                                      "Authorization": "Bearer {}".format(self.spotify_token)})

    def play_sad(self):
        # print ("Playing sad music :(")

        query = "https://api.spotify.com/v1/me/player/play?{}".format(self.device_id)
        data = json.dumps({"context_uri": self.sad_list,
                           "offset": {"position": 0},
                           "position_ms": 0})

        response = requests.put(query, data, headers={"Content-Type": "application/json",
                                                      "Authorization": "Bearer {}".format(self.spotify_token)})

    def play_surprise(self):
        # print ("Playing surprise music :O")

        query = "https://api.spotify.com/v1/me/player/play?{}".format(self.device_id)
        data = json.dumps({"context_uri": self.surprise_list,
                           "offset": {"position": 0},
                           "position_ms": 0})

        response = requests.put(query, data, headers={"Content-Type": "application/json",
                                                      "Authorization": "Bearer {}".format(self.spotify_token)})

    def call_refresh(self):
        # print ("Refreshing token...")

        refreshCaller = Refresh()
        self.spotify_token = refreshCaller.refresh()  # new access token created

        self.get_device_id()