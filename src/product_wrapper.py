

class ProductWrapper:
    def __init__(self, product):
        self.product = product
        self.title = product.title
        self.url = product.url
        self.price_value = product.prices.price.value
        self.price_display = product.prices.price.display
        self.is_adult = product.info.is_adult
        self.author = ''
        if product.info.contributors is not None and len(product.info.contributors) > 0:
            self.author = product.info.contributors[0].name

    def __eq__(self, other):
        return self.url == other.url

    def __hash__(self):
        return hash(self.url)

    def __lt__(self, other):
        return f'{self.author}:{self.title}' < f'{other.author}:{other.title}'

    def __gt__(self, other):
        return f'{self.author}:{self.title}' > f'{other.author}:{other.title}'

