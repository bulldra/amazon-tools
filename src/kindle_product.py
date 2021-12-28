#!/usr/bin/env python3

__version__ = "0.1.0"

import re

import kindle_util


class KindleProduct:
    def __init__(self, product=None):
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

        if product is not None:
            self.product = product
            self.asin = product.asin
            self.title = product.title
            self.series_title = kindle_util.norm_series_title(product.title)
            self.url = product.url
            self.price_value = product.prices.price.value
            self.price_display = product.prices.price.display
            self.authors = self._authors()
            self.author = self.authors[0]
            self.genles = self._genles()
            self.is_adult = product.info.is_adult

    def _authors(self):
        if (
            self.product.info.contributors is not None
            and len(self.product.info.contributors) > 0
        ):
            return [re.sub(r"\s", "", a.name) for a in self.product.info.contributors]
        else:
            return ["著者情報なし"]

    def _genles(self):
        return [
            self._genles_node([], node)
            for node in self.product.raw_info.browse_node_info.browse_nodes
        ]

    def _genles_node(self, genles, node):
        genles.insert(0, node.display_name)
        return (
            genles
            if node.ancestor is None
            else self._genles_node(genles, node.ancestor)
        )

    def __eq__(self, other):
        return self.asin == other.asin

    def __hash__(self):
        return hash(self.asin)

    def __lt__(self, other):
        return self.author < other.author

    def __gt__(self, other):
        return self.author > other.author

    def __str__(self):
        return f"{self.asin},{self.author},{self.title}"


def from_response(product):
    return KindleProduct(product)
