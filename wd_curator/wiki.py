import os
import pywikibot
import time
import yaml


class Wiki(object):

    """docstring for Wiki"""

    def __init__(self, options):
        super(Wiki, self).__init__()
        self.options = options
        meta_path = os.path.join(__file__, '../config/meta.yml')
        self.meta = yaml.load(open(meta_path, 'r'))
        self.items_checked = []

    @classmethod
    def from_config(cls, file):
        options = yaml.load(file)
        return cls(options)

    def run(forever=True):
        if not forever:
            self._run()
            return

        while True:
            self._run()
            time.sleep(3600)

    def _run(self):
        items = self._load_pages()
        for item in items:
            if item.getID() in self.items_checked:
                continue
            for check in self.meta['checks']:
                self.run_check(self.meta['checks'][check], item)
            for check in self.options['checks']:
                self.run_check(self.options['checks'][check], item)

    def _load_pages(self):
        file_path = os.path.join(__file__, '../data/{0}'.format(self.meta['dbname']))
        with open(file_path, 'r') as f:
            for line in f:
                line = line.replace('\n', '').replace('\r', '').strip()
                item = pywikibot.ItemPage(self.repo, 'Q' + line)
                try:
                    item.get()
                except pywikibot.NoPage:
                    continue
                yield item

    def run_check(self, check, item):

