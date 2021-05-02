class ProductWrapper:
    def __init__(self, product):
        self.raw = product
        self.asin = product.asin
        self.title = product.title
        self.url = product.url
        self.price_value = product.prices.price.value
        self.price_display = product.prices.price.display
        self.is_adult = product.info.is_adult
        self.authors = self._authors()
        self.author = self.authors[0]
        self.genles = self._genles()


    def _authors(self):
        authors = list()
        if self.raw.info.contributors is not None and len(self.raw.info.contributors) > 0:
            for a in self.raw.info.contributors:
                authors.append(a.name)
        if len(authors) == 0:
            authors.append('')
        return authors

    def _genles(self):
        genles = set()
        for node in self.raw.raw_info.browse_node_info.browse_nodes:
            self._genles_node(genles, node)
        return list(genles)

    def _genles_node(self, genles, node):
        genles.add(node.display_name)
        if node.ancestor is None:
            return genles
        else:
            return self._genles_node(genles, node.ancestor)

    def __eq__(self, other):
        return self.asin == other.asin

    def __hash__(self):
        return hash(self.asin)

    def __lt__(self, other):
        return f'{self.author}:{self.title}' < f'{other.author}:{other.title}'

    def __gt__(self, other):
        return f'{self.author}:{self.title}' > f'{other.author}:{other.title}'
