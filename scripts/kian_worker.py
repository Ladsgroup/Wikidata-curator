import kian.fitness
import os
import pywikibot

from kian import TrainedModel

from wd_curator import Worker


class KianWorker(Worker):
    """docstring for KianWorker"""
    def __init__(self, name):
        model = TrainedModel.from_file(name)
        model.load()
        file_path = os.path.join(model.data_directory, 'res2.dat')

        if not os.path.isfile(file_path):
            raise ValueError('You should train the model first')
        with codecs.open(file_path, 'r', 'utf-8') as f:
            cv_set = eval(f.read())
        self.thrashhold = kian.fitness.optimum_thrashhold(cv_set, 0.25)[0]
        self.model = model
        super(KianWorker, self).__init__('KianWorker:' + name, model.wiki)

    def _run(self):
        for item in self._load_pages():
            if self.wiki not in item.sitelinks:
                continue
            page = item.sitelinks[self.wiki]
            cats = [cat.title(underscore=True, withNamespace=False)
                    for cat in page.categories()]
            features = self.model.label_case(cats)
            res = Kian.kian(self.model.theta, features)[0]
            if res > second_thrashhold:
                claim = pywikibot.Claim(self.repo, self.model.property_name)
                claim.setTarget(pywikibot.ItemPage(self.repo, self.model.value))
                item.addClaim(claim, summary='Bot: Adding %s:%s from %s '
                              '([[User:Ladsgroup/Kian|Powered by Kian]])' %
                              (self.model.property_name, self.model.value, self.wiki))
                source = pywikibot.Claim(self.repo, 'P143')
                source.setTarget(pywikibot.ItemPage(self.repo, self.sources[self.wiki]))
                claim.addSource(source)
