import requests

from config import settings


class TelegramNotificationBot:
    """
    A class to facilitate sending messages through the Telegram Bot API.

    Attributes:
        URL (str): The base URL for Telegram API.
        TOKEN (str): The authentication token for the Telegram bot.

    Methods:
        send_telegram_message(cls, text, chat_id) -> None: Sends a message via Telegram.
    """

    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_TOKEN

    @classmethod
    def send_telegram_message(cls, text, chat_id) -> None:
        """
        Sends a message using the Telegram Bot API.

        Args:
            cls: Class object.
            text (str): The text content of the message.
            chat_id (int or str): The chat ID to which the message will be sent.
        """
        requests.post(
            url=f'{cls.URL}{cls.TOKEN}/sendMessage',
            data={
                'chat_id': chat_id,
                'text': text
            }
        )
