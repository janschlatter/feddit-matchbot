import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from football_api.data_client import FootballDataClient
from football_api.data_utils import parse_matches
from config.settings import api_key

SEASON = 2023
LEAGUE_ID = 8
TEAM_ID = 1719


# Create an instance of the FootballDataClient
client = FootballDataClient(api_key)

# Get the matches for the specified league
matches_data = client.get_matches(LEAGUE_ID, SEASON)

# Parse the matches data
matches = parse_matches(matches_data)

# # Print the matches
# for match in matches:
#     print(match)

# Get the next fixture for the specified team
next_fixture_data = client.get_next_fixture(TEAM_ID, SEASON, LEAGUE_ID)

# Parse the next fixture data
next_fixture = parse_matches(next_fixture_data)

# Print the next fixture
print(next_fixture)
