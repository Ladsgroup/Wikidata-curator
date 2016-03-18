class Worker(object):
    """docstring for Worker"""
    def __init__(self, name, wiki):
        super(Worker, self).__init__()
        self.name = name
        self.wiki = wiki
        self._cache = []

