import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    alpari_email = os.getenv("alpari_email")
    alpari_password = os.getenv("alpari_password")
    # main chanel bot
    bot_api_key = os.getenv("bot_api_key")
    channel_id = os.getenv("channel_id")
