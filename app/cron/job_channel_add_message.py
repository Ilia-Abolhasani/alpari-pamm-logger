from app.util.Message import create_message


def start(alpari, bot_api):
    try:
        accounts = alpari.get_acounts_list()
        message = create_message(accounts)
        result = bot_api.send_message(message)
        message_id = result.message_id
    except Exception as error:
        print(error)
