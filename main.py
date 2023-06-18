from config.settings import (
    api_key,
    LEMMY_USERNAME,
    LEMMY_BASE_URL,
    LEMMY_PASSWORD,
    COMMUNITY_ID,
)
from football_api.data_client import FootballDataClient
from football_api.data_utils import parse_matches
from lemmy_api.lemmy_client import LemmyClient
from bot.thread_creation import create_match_threads

# Football API
SEASON = 2023
TEAM_ID = 1719
LEAGUE_ID = 8

try:
    # Create an instance of the FootballDataClient
    client = FootballDataClient(api_key)

    # Get the matches for the specified league
    matches_data = client.get_next_fixture(TEAM_ID, SEASON, LEAGUE_ID)

    # Parse the matches data
    matches = parse_matches(matches_data)

    print(
        "Successfully processed match:",
        matches[0]["home_team"],
        "–",
        matches[0]["away_team"],
        "at",
        matches[0]["date"],
    )  # Debug print

    try:
        # Create an instance of the LemmyClient
        lemmy_client = LemmyClient(LEMMY_BASE_URL, LEMMY_USERNAME, LEMMY_PASSWORD)

        print("Lemmy token:", lemmy_client.token)  # Debug print

        # Create match threads on Lemmy
        create_match_threads(lemmy_client, matches, COMMUNITY_ID)
    except Exception as e:
        print(f"Lemmy response: {e}")  # Debug print
except Exception as e:
    print(f"Lemmy response: {e}")  # Debug print
