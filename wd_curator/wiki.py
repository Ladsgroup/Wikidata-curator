import json
import os
import pywikibot

from .check import Check
from .worker import Worker


class WikiWorker(Worker):

    """docstring for Wiki"""

    def __init__(self, options, meta, data_path=None):
        self.options = options
        for check in options['checks']:
            self.options['checks'][check] = Check(
                check, *options['checks'][check])
        self.meta = meta
        for check in meta['checks']:
            self.meta['checks'][check] = Check(check, *meta['checks'][check])
        self.site = pywikibot.Site(options['lang'], options['family'])
        repo = self.site.data_repository()
        super(WikiWorker, self).__init__(
            'WikiWorker:' + self.options['dbname'], self.options['dbname'],
            data_path, repo)

    @classmethod
    def from_config(cls, file):
        options = json.load(file)
        meta_path = os.path.join(os.path.dirname(file.name), 'meta.json')
        data_path = os.path.join(os.path.dirname(file.name), '../data')
        return cls(options, json.load(open(meta_path, 'r')), data_path)

    def _run(self):
        items = self._load_pages()
        for item in items:
            for check in self.meta['checks']:
                self.run_check(self.meta['checks'][check], item)
            for check in self.options['checks']:
                self.run_check(self.options['checks'][check], item)

    def run_check(self, check, item):
        try:
            item.get()
        except pywikibot.NoPage:
            return
        except pywikibot.isRedirectPage:
            return
        page_name = item.sitelinks.get(self.options['dbname'])
        if not page_name:
            return
        page = pywikibot.Page(self.site, page_name)
        try:
            page.get()
        except:
            return
        check.run()
