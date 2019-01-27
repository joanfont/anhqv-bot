from telegram.ext import Updater, InlineQueryHandler

from .api import ClipsAPI
from .config import config
from .inline import ClipSearch


clips_api = ClipsAPI(config.CLIPS_API_BASE_URL)


class ANHQVBot:

    def __init__(self, token):
        self.updater = Updater(token=token)

    def start(self):
        self._configure_callbacks()
        self.updater.start_polling()
        self.updater.idle()

    def stop(self):
        self.updater.stop()

    def _configure_callbacks(self):
        clip_search = ClipSearch(clips_api)

        self.updater.dispatcher.add_handler(
            InlineQueryHandler(clip_search.handle)
        )
