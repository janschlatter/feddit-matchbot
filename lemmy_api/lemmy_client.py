import requests


class LemmyClient:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.token = self.get_token()

    def get_token(self):
        url = f"{self.base_url}/api/v3/user/login"
        data = {"username_or_email": self.username, "password": self.password}
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()  # Debug print
            return response.json()["jwt"]
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while getting token: {e}")
            raise

    def create_post(self, title, content, community_id):
        print("Creating post...")  # Debug print
        url = f"{self.base_url}/api/v3/post"
        data = {
            "name": title,
            "content": content,
            "community_id": community_id,
            "auth": self.token,  # Add the auth field with the token
        }
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()  # Debug print
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Lemmy Response: {e}")  # Debug print
            raise
