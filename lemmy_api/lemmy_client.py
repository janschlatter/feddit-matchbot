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
        response = requests.post(url, json=data)
        print(response.content)
        return response.json()["jwt"]

    def create_post(self, title, content, community_id):
        print("Creating post...")  # Debug print
        url = f"{self.base_url}/api/v3/post"
        data = {
            "name": title,
            "content": content,
            "community_id": community_id,
            "auth": self.token,  # Add the auth field with the token
        }
        response = requests.post(url, json=data)
        print("Lemmy API response status code:", response.status_code)  # Debug print
        print("Raw Lemmy API response:", response.content)  # Debug print
        return response.json()
