import json
import os
import pywikibot
import time

from wd_curator import Worker


class WikiWorker(Worker):

    """docstring for Wiki"""

    def __init__(self, options):
        self.options = options
        meta_path = os.path.join(__file__, '../config/meta.json')
        self.meta = json.load(open(meta_path, 'r'))
        super(Wiki, self).__init__('WikiWorker:' + self.options['dbname'], self.options['dbname'])

    @classmethod
    def from_config(cls, file):
        options = json.load(file)
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
            for check in self.meta['checks']:
                self.run_check(self.meta['checks'][check], item)
            for check in self.options['checks']:
                self.run_check(self.options['checks'][check], item)

    def run_check(self, check, item):

