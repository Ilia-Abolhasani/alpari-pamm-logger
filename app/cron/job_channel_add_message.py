from app.util.Message import create_message


def start(alpari, bot_api, latest_message_file_handler):
    try:
        accounts = alpari.get_acounts_list()
        message = create_message(accounts)
        latest_message = latest_message_file_handler.read()
        if message == latest_message:
            return
        result = bot_api.send_message(message)
        latest_message_file_handler.write(message)
    except Exception as error:
        print(error)
