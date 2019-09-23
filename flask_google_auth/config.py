import os
import requests

class Config:
    def __init__(self):
        # You must configure these 3 values from Google APIs console
        # https://code.google.com/apis/console
        self.GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
        self.GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')
        self.GOOGLE_REDIRECT_URI = os.environ.get('GOOGLE_REDIRECT_URI', '/oauth2callback')


        self.google_userinfo_url = self.get_google_userinfo_url()
        # App configs
        self.FLASK_SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'development')
        self.DEBUG =  os.environ.get('FLASK_DEBUG', False)


    def get_google_userinfo_url(self):
        # Try to get the current endpoint from Google at startup, else use what we think it is.
        response = requests.get('https://accounts.google.com/.well-known/openid-configuration')
        if response.ok:
            print(f'Using endpoint {response.json()["userinfo_endpoint"]} for Google User Info')
            return response.json()['userinfo_endpoint']
        return 'https://openidconnect.googleapis.com/oauth2/v1/userinfo'

config = Config()
