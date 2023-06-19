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

    def get_next_fixture(self, TEAM_ID, SEASON, LEAGUE_ID):
        url = f"{self.base_url}/fixtures?season={SEASON}&league={LEAGUE_ID}&team={TEAM_ID}&next=1"
        headers = {
            "x-rapidapi-key": api_key,
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
