from functions import RiotAPI
import constants as consts
import time

def main():

   api = RiotAPI ('YOUR API KEY GOES HERE')
   static_api = RiotAPI ('YOUR API KEY ALSO GOES HERE')

   summoner_name = input ('Enter a Summoner who is in a live game: ')
   standardized_summoner_name = (summoner_name.replace(" ", "")).lower()

   summoner_information = api.get_summoner_by_name (standardized_summoner_name) 

   summoner_id = summoner_information[standardized_summoner_name]['id']
   live_game = api.get_live_game (summoner_id)

   blue_team = []
   purple_team = []

   for player in live_game['participants']:
      player_info = {'summonerId' : player['summonerId'], 'summonerName' : player['summonerName']}
      if player['teamId'] == 100:
         blue_team.append(player_info)
      else: 
         purple_team.append(player_info)

   print ("BLUE TEAM: ")
   for player in blue_team:
      print (player['summonerName'])
      player_recent_games = api.get_recent_games (player['summonerId'])
      for outcome_of_game in player_recent_games['games']:
         if str(outcome_of_game['stats']['win']) == "False":
            print ("LOSS")
         else:
            print ("WIN")
      print ("\n\n")
      time.sleep (1.0)

   print ("\n\nPURPLE TEAM: ")
   for player in purple_team:      
      print (player['summonerName'])
      player_recent_games = api.get_recent_games (player['summonerId'])
      for outcome_of_game in player_recent_games['games']:
         if str(outcome_of_game['stats']['win']) == "False":
            print ("LOSS")
         else:
            print ("WIN")
      print ("\n\n")
      time.sleep (1.0)

if __name__ == "__main__":
   main()
