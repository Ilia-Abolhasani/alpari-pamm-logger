from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import app.cron.job_channel_add_message as job_channel_add_message


def start_jobs(alpari, bot_api, latest_message_file_handler):
    scheduler = BackgroundScheduler(
        {'apscheduler.job_defaults.max_instances': 1})
    # job add message to channel
    scheduler.add_job(
        lambda: job_channel_add_message.start(
            alpari, bot_api, latest_message_file_handler),
        trigger=CronTrigger.from_crontab('*/5 * * * *')
    )
    scheduler.start()
