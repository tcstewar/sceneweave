
class Choices(object):
    def __init__(self):
        self.options = []
    def add(self, **kwargs):
        assert len(kwargs) == 1
        k, v = kwargs.items()[0]
        self.options.append((k, v))

