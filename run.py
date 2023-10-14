from app.cron.manager import start_jobs
from app.util.BotAPI import BotAPI
from app.config.config import Config

if __name__ == '__main__':
    bot_api = BotAPI(
        Config.bot_api_key,
        Config.bot_chat_id
    )
    start_jobs(bot_api)
