#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
        self.genles = self._genles()
        self.is_adult = product.info.is_adult

    def _authors(self):
        if self.product.info.contributors is not None and len(self.product.info.contributors) > 0:
            return [a.name for a in self.product.info.contributors]
        else:
            ['著者情報なし']

    def _genles(self):
        return [self._genles_node([], node) for node in self.product.raw_info.browse_node_info.browse_nodes]

    def _genles_node(self, genles, node):
        genles.insert(0, node.display_name)
        return genles if node.ancestor is None else self._genles_node(genles, node.ancestor)

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
