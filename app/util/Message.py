def create_message(accounts):
    message = ""
    for name in accounts:
        message += f"<b>{name}: {accounts[name]}</b> \n"
    return message
