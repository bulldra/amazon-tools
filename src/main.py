#!/usr/bin/env python3
__version__ = "0.1.0"

import argparse
import logzero
import settings
from product_wrapper import ProductWrapper
from amazon.paapi import AmazonAPI

class Main:
    def __init__(self):
        logzero.logfile(
            settings.settings_dict['logfile'],
            loglevel=20,
            maxBytes=1e6,
            backupCount=3
        )
        self.logger = logzero.logger

    def main(self, args):
        self.logger.info(args)
        node = args.arg1
        amazon_api = AmazonAPI(settings.amazon_access_key, settings.amazon_secret_key, settings.amazon_assosiate_id, 'JP')
        result = set()
        now_price = settings.min_price
        min_price = 0
        for i in range(0, 10):
            if min_price == now_price * 100:
                now_price += 1
            min_price = now_price * 100
            for page in range(1, 11):
                products = amazon_api.search_products(
                    browse_node=node,
                    item_page=page,
                    min_price=min_price,
                    sort_by='Price:LowToHigh'
                )
                if products is None:
                    self.logger.info(f'response {products}')
                    break
                self.logger.info(f'response {len(products)} items')
                for x in products:
                    p = ProductWrapper(x)
                    result.add(p)
                    now_price = p.price_value
            else:
                continue
            break

        with open(settings.outfile, 'w', encoding='utf-8') as out:
            out.write('author,title,price,url,genles\n')
            for x in filter(lambda x : self.is_need(x), sorted(result)):
                out.write(f'"{x.author}","{x.title}","{x.price_display}","{x.url}","{x.genles}"\n')

    def is_need(self, product):
        flag = len(set(product.genles) & set(settings.genle_black_list)) == 0 \
            and len(set(product.authors) & set(settings.author_black_list)) == 0 \
            and len([x for x in settings.title_black_list if x in product.title]) == 0
        if flag == False:
            self.logger.info(f'結果除外 {product.title}')
        return flag

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version="%(prog)s (version {version})".format(version=__version__))
    parser.add_argument("arg1", help='Amazon Node')
    args = parser.parse_args()
    Main().main(args)
