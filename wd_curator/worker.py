import os
import pywikibot
import time


class Worker(object):
    """docstring for Worker"""
    def __init__(self, name, wiki):
        super(Worker, self).__init__()
        self.name = name
        self.wiki = wiki
        self._items_checked = []

    def _load_pages(self):
        file_path = os.path.join(__file__,
                                 '../data/{0}'.format(self.options['dbname']))
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

    def run(self, forever=True, really_forever=False):
        if really_forever:
            print('Are you sure?')
            try:
                self.run(forever, False)
            except:
                print('Got an error, re-running in 10 seconds')
                time.sleep(10)
                self.run(forever, True)

        if not forever:
            self._run()
            return

        while True:
            self._run()
            time.sleep(3600)
