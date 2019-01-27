from telegram import InlineQueryResultVideo, InputTextMessageContent

from .api import ClipsAPI
from .utils import get_youtube_video_thumbnail


class Inline:

    def handle(self, bot, update):
        raise NotImplementedError()


class ClipSearch(Inline):

    def __init__(self, clips_api):
        self.clips_api = clips_api

    def handle(self, bot, update):
        query = update.inline_query.query
        results = self.clips_api.search(query)
        inline_results = list(map(self._clip_to_result, results))
        update.inline_query.answer(inline_results)

    def _clip_to_result(self, clip):
        thumb_url = get_youtube_video_thumbnail(clip.link)
        return InlineQueryResultVideo(
            id=clip.id,
            title=clip.title,
            video_url=clip.url,
            thumb_url=get_youtube_video_thumbnail(clip.link),
            mime_type='text/html',
            input_message_content=InputTextMessageContent(clip.url)
        )