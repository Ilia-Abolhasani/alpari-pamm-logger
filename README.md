# Alpari PAMM Logger

This is a Python project for monitoring Alpari PAMM accounts and sending updates to a Telegram channel.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Ilia-Abolhasani/alpari-pamm-logger.git
   cd alpari-pamm-logger
   ```

2. Install the required Python packages from the requirements.txt file:
  ```bash
  pip install -r requirements.txt
  ```

3. Create a .env file from the provided .env.template and fill in the necessary information:
  ```bash
    # Alpari
    alpari_email = ""
    alpari_password = ""
    # Telegram Bot API Key
    bot_api_key = ""
    channel_id = ""
  ```

## Setting up the Telegram Bot

To use the Telegram bot for sending updates, follow these steps:

1. **Create a Telegram bot using BotFather:**

   - Visit [BotFather](https://core.telegram.org/bots#botfather) on Telegram and follow the instructions to create a new bot.
   - Once your bot is created, you will receive a `bot_api_key`. Keep this key for the next steps.

2. **Create a private channel on Telegram:**

   - In Telegram, create a private channel where you want to receive the updates.

3. **Add the Telegram bot to the channel as an admin:**

   - In your private channel, go to the "Members" section and add the Telegram bot you created as an admin. This step is necessary for the bot to send messages to the channel.

4. **Find the `channel_id` using the username_to_id_bot:**

   - You can use the [username_to_id_bot](https://t.me/username_to_id_bot) in Telegram to find the `channel_id` for your private channel. This ID is required in your `.env` file to specify the destination channel for updates.
## Running the Project

After setting up the Telegram bot and filling in the `.env` file, you can run the project using the following command:

```bash
python3 run.py
```

The project will check Alpari PAMM accounts every 5 minutes. If any changes occur in the account values, it will send the latest values to the Telegram channel. You can adjust the 5-minute interval by modifying the cron job in app/cron/manager.py based on your requirements.

To check the Alpari accounts, the project uses a web scraper that logs into the Alpari account, retrieves the HTML, and searches through it for changes.

Feel free to customize and improve the project as needed for your specific use case.


## **⚠️ Caution: Use at Your Own Risk ⚠️**

Please be aware that this project involves handling sensitive information, such as your Alpari login credentials, and automating actions on your accounts. It is important to exercise caution and consider the following:

- **Security**: Be extremely cautious with your Alpari login information. Ensure that you do not share your `.env` file or any sensitive data with others.

- **Risk**: Using this project to automate actions on your Alpari accounts carries inherent risks. Be aware of the potential risks involved and only use it if you fully understand and accept those risks.

- **Financial Responsibility**: You are solely responsible for the consequences of using this project, including any financial implications. Make sure you are well-informed and understand the potential outcomes.

- **Legal Compliance**: Ensure that using this project complies with Alpari's terms of service and any applicable laws and regulations in your jurisdiction.

By using this project, you acknowledge and accept the responsibility for your actions and the potential risks involved. The project author and contributors are not responsible for any consequences that may arise from its use.
