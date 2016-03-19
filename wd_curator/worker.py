import pywikibot

class Worker(object):
    """docstring for Worker"""
    def __init__(self, name, wiki):
        super(Worker, self).__init__()
        self.name = name
        self.wiki = wiki
        self._items_checked = []

    def _load_pages(self):
        file_path = os.path.join(__file__, '../data/{0}'.format(self.meta['dbname']))
        with open(file_path, 'r') as f:
            for line in f:
                line = line.replace('\n', '').replace('\r', '').strip()
                if 'Q' + line in self._items_checked:
                    continue
                item = pywikibot.ItemPage(self.repo, 'Q' + line)
                try:
                    item.get()
                except pywikibot.NoPage:
                    self._items_checked.append(item.getID())
                    continue
                yield item

    def run(forever=True):
        if not forever:
            self._run()
            return

        while True:
            self._run()
            time.sleep(3600)
