import decouple


class Config:

    @property
    def CLIPS_API_BASE_URL(self):
        return decouple.config('CLIPS_API_BASE_URL')

    @property
    def TELEGRAM_TOKEN(self):
        return decouple.config('TELEGRAM_TOKEN')



config = Config()
