from app.cron.manager import start_jobs
from app.util.BotAPI import BotAPI
from app.config.config import Config
from app.util.Alpari import Alpari

if __name__ == '__main__':
    alpari = Alpari(Config.alpari_email, Config.alpari_password)
    bot_api = BotAPI(
        Config.bot_api_key,
        Config.channel_id
    )
    start_jobs(alpari, bot_api)
