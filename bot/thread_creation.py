from lemmy_api.lemmy_client import LemmyClient
from lemmy_api.lemmy_utils import format_match_post


def create_match_threads(lemmy_client, matches, community_id):
    print("Creating match threads...")  # Debug print
    for match in matches:
        title, content = format_match_post(match)
        response = lemmy_client.create_post(title, content, community_id)
        print(f"Created post: {title}")
        print(f"Post URL: {response['post']['url']}")
