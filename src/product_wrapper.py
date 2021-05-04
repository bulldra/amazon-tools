import settings
import logzero
import kindle_util

class ProductWrapper:
    def __init__(self, product):
        logzero.logfile(
            settings.settings_dict['logfile'],
            loglevel=20,
            maxBytes=1e6,
            backupCount=3
        )
        self.logger = logzero.logger
        self.product = product
        self.asin = product.asin
        self.title = product.title
        self.series_title = kindle_util.tlanslate_series_title(product.title)
        self.url = product.url
        self.price_value = product.prices.price.value
        self.price_display = product.prices.price.display
        self.authors = self._authors()
        self.author = self.authors[0]
        self.genles = self._genles()
        self.is_adult = product.info.is_adult

    def _authors(self):
        authors = list()
        if self.product.info.contributors is not None and len(self.product.info.contributors) > 0:
            for a in self.product.info.contributors:
                authors.append(a.name)
        if len(authors) == 0:
            authors.append('')
        return authors

    def _genles(self):
        genles = set()
        for node in self.product.raw_info.browse_node_info.browse_nodes:
            self._genles_node(genles, node)
        return list(genles)

    def _genles_node(self, genles, node):
        genles.add(node.display_name)
        if node.ancestor is None:
            return genles
        else:
            return self._genles_node(genles, node.ancestor)

    def predict_filtered(self):
        cause_dict = {}
        cause_dict['adult'] = 0.2 if self.is_adult else 0.0
        cause_dict['genle'] = len(set(self.genles) & set(settings.genle_black_list)) * 0.2
        cause_dict['author'] = len(set(self.authors) & set(settings.author_black_list)) * 0.2
        cause_dict['title'] = len([x for x in settings.title_black_list if x in self.title]) * 0.2
        cause_dict['having'] = len(set([self.asin]) & set(settings.amazon_list)) * 1
        socore = min(sum(cause_dict.values()), 1.0)
        if  socore >= 0.2:
            self.logger.info(f'filterd by {cause_dict} {self.asin} {self.author} {self.title}')
            return True
        else:
            return False

    def __eq__(self, other):
        return self.asin == other.asin
    def __hash__(self):
        return hash(self.asin)
    def __lt__(self, other):
        return self.title < other.title
    def __gt__(self, other):
        return self.title > other.title
