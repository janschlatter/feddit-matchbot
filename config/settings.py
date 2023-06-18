from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
api_key = os.getenv("api_key")
LEMMY_USERNAME = os.getenv("LEMMY_USERNAME")
LEMMY_PASSWORD = os.getenv("LEMMY_PASSWORD")
LEMMY_BASE_URL = os.getenv("LEMMY_BASE_URL")
COMMUNITY_ID = int(os.getenv("COMMUNITY_ID"))
