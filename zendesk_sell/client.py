import requests
import json

class Client(object):

    API_BASE = 'https://api.getbase.com'

    def __init__(self, access_token, api_version='v2'):
        self.access_token = access_token
        self.api_version = api_version
        self.base_uri = "{}/{}".format(self.API_BASE, api_version)

    def get(self, path, params={}):
        response = requests.get(self.build_uri(path), params=params, headers=self.headers())
        return response

    def build_uri(self, path):
        return "{}/{}".format(self.base_uri, path)

    def headers(self):
        return {
            'Accept' : 'application/json',
            'Authorization' : self.authorization_header_value()
        }

    def authorization_header_value(self):
        return "Bearer {}".format(self.access_token)