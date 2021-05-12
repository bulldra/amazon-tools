#!/usr/bin/env python3
__version__ = "0.1.0"

import kindle_util
import simhash

class KindleProduct:
    def __init__(self):
        self.product = None
        self.asin = None
        self.title = None
        self.series_title = None
        self.url = None
        self.price_value = 0.0
        self.price_display = 0.0
        self.authors = None
        self.author = None
        self.genles = None
        self.is_adult = None

    def from_amazon_product(self, product):
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

    def simhash(self):
        return simhash.Simhash(self.title)
    def __eq__(self, other):
        return self.asin == other.asin
    def __hash__(self):
        return hash(self.asin)
    def __lt__(self, other):
        return self.title < other.title
    def __gt__(self, other):
        return self.title > other.title
