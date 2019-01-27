
from urllib.parse import urlencode

import requests

from .entities import Clip


class ClipsAPI:

    SEARCH_PATH = '/api/clips-search/'

    def __init__(self, base_url):
        self.base_url = base_url

    def search(self, query):
        url = self._build_url(self.SEARCH_PATH, {
            'query': query
        })

        response = requests.get(url)
        data = response.json()

        return list(map(lambda x: Clip(**x), data))

    def _build_url(self, path, params={}):
        url = f'{self.base_url}{path}'

        if params:
            qs = urlencode(params)
            url = f'{url}?{qs}'

        return url
