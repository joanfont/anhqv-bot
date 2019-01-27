
class Clip:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.link = kwargs.get('link')

        self.title = kwargs.get('title')

        self.start = kwargs.get('start')
        self.end = kwargs.get('end')

    @property
    def url(self):
        return f'{self.link}&start={self.start}'
