from app.cron.manager import start_jobs
from app.util.BotAPI import BotAPI
from app.config.config import Config
from app.util.Alpari import Alpari
from app.util.FileHelper import FileHelper
import time

if __name__ == '__main__':
    alpari = Alpari(Config.alpari_email, Config.alpari_password)
    bot_api = BotAPI(
        Config.bot_api_key,
        Config.channel_id
    )
    latest_message_file_handler = FileHelper("./latest_message.txt")
    start_jobs(alpari, bot_api, latest_message_file_handler)
    while True:
        time.sleep(5)
