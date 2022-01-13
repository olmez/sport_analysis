import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class access_token_from_strava:

    def __init__(self):
        self.auth_url = "https://www.strava.com/oauth/token"
        self.activities_url = "https://www.strava.com/api/v3/athlete/activities"

        #replace variables with values for your account
        self.payload = {
                        'client_id': "76573",
                        'client_secret': 'a7dd81bb0d2f94137806ed32e885298d34b5e77b',
                        'refresh_token': '14213e4695997f385384b8a35c5d8d4039266e0d',
                        'grant_type': "refresh_token",
                        'f': 'json'
                        }

        self.access_token = None
        self.header = None
        self.param = None
        self.activities_data = None

    def request_token(self):
        print("Requesting Token...")
        res = requests.post(self.auth_url, data=self.payload, verify=False)
        self.access_token = res.json()['access_token']
        print("Access Token = {}".format(self.access_token))

    def get_activities_data(self):
        self.header = {'Authorization': 'Bearer ' + self.access_token}
        self.param = {'per_page': 200, 'page': 1}
        self.activities_data = requests.get(self.activities_url, headers=self.header, params=self.param).json()

    def run(self):
        self.request_token()
        self.get_activities_data()
