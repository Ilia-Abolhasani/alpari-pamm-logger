from app.util.Message import create_message


def start(bot_api):
    global job_lock
    with job_lock:
        try:
            message = create_message()
            result = bot_api.send_message(message)
            message_id = result.message_id
        except Exception as error:
            print(error)
