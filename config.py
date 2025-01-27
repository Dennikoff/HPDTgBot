import os
from dotenv import load_dotenv

load_dotenv()
load_dotenv('.env.local', override=True)

token = os.getenv("TOKEN")
channel_id = os.getenv("CHANNEL_ID")
channel_url = os.getenv("CHANNEL_URL")