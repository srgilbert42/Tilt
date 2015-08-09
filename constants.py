URL = {
   'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
   'static_base': 'https://{proxy}.api.pvp.net/api/lol/static-data/{region}/{url}',
   'spectator': 'https://{proxy}.api.pvp.net/{url}',

   'summoner_by_name': 'v{version}/summoner/by-name/{names}',
   'league_by_id': 'v{version}/league/by-summoner/{ids}/entry',
   'champion_by_id': 'v{version}/champion/{ids}',
   'free_champions' : 'v{version}/champion',
   'match_history' : 'v{version}/matchhistory/{ids}',
   'game_by_summoner' : 'v{version}/game/by-summoner/{ids}/recent',
   'current_game_by_id' : 'observer-mode/rest/consumer/getSpectatorGameInfo/NA1/{ids}'
}

API_VERSIONS = {
   'summoner': '1.4',
   'league': '2.5',
   'static-data' : '1.2',
   'champion': '1.2',
   'matchhistory' : '2.2',
   'game' : '1.3',
   'current-game' : '1.0'
}

REGIONS = {
   'north_america': 'na', 
   'global' : 'global'
}
