import requests
from config.settings import api_key


class FootballDataClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api-football-v1.p.rapidapi.com/v3"

    def get_matches(self, LEAGUE_ID, SEASON):
        url = f"{self.base_url}/fixtures?league={LEAGUE_ID}&season={SEASON}"
        headers = {
            "x-rapidapi-key": api_key,
            "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def get_next_fixtures(self, team_id, season, league_id, num_fixtures=1):
        url = f"{self.base_url}/fixtures?season={season}&league={league_id}&team={team_id}&next={num_fixtures}"
        headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def get_teams(self, league_id, season):
        url = f"{self.base_url}/teams?league={league_id}&season={season}"
        headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
        }
        response = requests.get(url, headers=headers)
        return response.json()
