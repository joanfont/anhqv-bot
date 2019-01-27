import logging

from anhqv_bot.config import config
from anhqv_bot.core import ANHQVBot

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

bot = ANHQVBot(config.TELEGRAM_TOKEN)

if __name__ == '__main__':
    try:
        bot.start()
    except KeyboardInterrupt:
        exit(1)