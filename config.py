import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
channel_id = os.getenv("CHANNEL_ID")