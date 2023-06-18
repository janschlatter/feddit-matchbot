from config.settings import api_key
from football_api.data_client import FootballDataClient
from football_api.data_utils import parse_matches
from lemmy_api.lemmy_client import LemmyClient
from bot.thread_creation import create_match_threads

# Football API
SEASON = 2023
TEAM_ID = 1719
LEAGUE_ID = 8

# Lemmy API
LEMMY_BASE_URL = "https://feddit.de"
LEMMY_USERNAME = "legende.dolch.0i@icloud.com"
LEMMY_PASSWORD = "h12ZNrGcMp@PAiUS9cgQ&0V3^qek%!Wg"
COMMUNITY_ID = 25689

# Create an instance of the FootballDataClient
client = FootballDataClient(api_key)

# Get the matches for the specified league
matches_data = client.get_next_fixture(TEAM_ID, SEASON, LEAGUE_ID)

# Parse the matches data
matches = parse_matches(matches_data)

print("Successfully processed matches:", matches)  # Debug print

# Create an instance of the LemmyClient
lemmy_client = LemmyClient(LEMMY_BASE_URL, LEMMY_USERNAME, LEMMY_PASSWORD)

print("Lemmy token:", lemmy_client.token)  # Debug print

# Create match threads on Lemmy
create_match_threads(lemmy_client, matches, COMMUNITY_ID)
