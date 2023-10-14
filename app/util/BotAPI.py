from pytgbot import Bot


class BotAPI:
    def __init__(self, bot_api_key, bot_chat_id):
        self.bot = Bot(bot_api_key)
        self.chat = bot_chat_id

    def send_message(self, text, parse_mode="HTML"):
        result = self.bot.send_message(self.chat, text, parse_mode)
        return result

    def edit_message_text(self, text, message_id, parse_mode="HTML"):
        result = self.bot.edit_message_text(
            text=text, chat_id=self.chat, message_id=message_id, parse_mode=parse_mode)
        return result

    def delete_message(self, message_id):
        result = self.bot.delete_message(self.chat, message_id)
        return result

    def pin_chat_message(self, message_id, disable_notification):
        result = self.bot.pin_chat_message(
            self.chat, message_id, disable_notification)
        return result
