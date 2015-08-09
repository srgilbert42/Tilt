import requests
import constants as consts

class RiotAPI (object):

   def __init__ (self, api_key, region=consts.REGIONS['north_america']):
      self.api_key = api_key
      self.region = region

   def _request (self, api_url, params={}):
      args = {'api_key': self.api_key}
      for key, value in params.items():
         if key not in args:
            args[key] = value

      response = requests.get (
         consts.URL['base'].format(
            proxy = self.region, 
            region = self.region,
            url = api_url
            ), 
         params = args
         )
      return response.json()
      
   def _spectator_request (self, api_url, params={}):
      args = {'api_key': self.api_key}
      for key, value in params.items():
         if key not in args:
            args[key] = value

      response = requests.get (
         consts.URL['spectator'].format(
            proxy = self.region,
            url = api_url
            ),
         params = args
         )
      return response.json()

   def get_summoner_by_name(self, name):
      api_url = consts.URL['summoner_by_name'].format(
         version = consts.API_VERSIONS['summoner'],
         names = name
      )
      return self._request(api_url)

   def get_recent_games (self, id):
      api_url = consts.URL['game_by_summoner'].format(
         version = consts.API_VERSIONS['game'],
         ids = id
      )
      return self._request(api_url)

   def get_live_game (self, id):
      api_url = consts.URL['current_game_by_id'].format(
         ids = id
         )
      return self._spectator_request(api_url)
