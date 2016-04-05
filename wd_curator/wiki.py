import json
import os
import pywikibot

from wd_curator import Check, Worker


class WikiWorker(Worker):

    """docstring for Wiki"""

    def __init__(self, options, meta):
        self.options = options
        for check in options['checks']:
            self.options['checks'][check] = Check(
                check, *options['checks'][check])
        self.meta = meta
        for check in meta['checks']:
            self.meta['checks'][check] = Check(check, *meta['checks'][check])
        self.site = pywikibot.Site(options['lang'], options['family'])
        super(WikiWorker, self).__init__(
            'WikiWorker:' + self.options['dbname'], self.options['dbname'])

    @classmethod
    def from_config(cls, file):
        options = json.load(file)
        meta_path = os.path.join(__file__, '../config/meta.json')
        return cls(options, json.load(open(meta_path, 'r')))

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
            continue
        except pywikibot.isRedirectPage:
            continue
        page_name = item.sitelinks.get(self.options['dbname'])
        if not page_name:
            continue
        page = pywikibot.Page(self.site, page_name)
        try:
            page.get()
        except:
            continue
        check.run()
