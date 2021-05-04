#!/usr/bin/env python3
__version__ = "0.1.0"

import argparse
import logzero
import settings
import math
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
        product_set = self.crawl_product_set(node, settings.max_item_num, settings.min_price)
        self.out_product_set(product_set, settings.outfile)

    def crawl_product_set(self, node, max_item_num, min_price):
        amazon_api = AmazonAPI(
            settings.amazon_access_key,
            settings.amazon_secret_key,
            settings.amazon_assosiate_id,
            'JP'
        )
        product_set = set()
        now_price = min_price
        request_min_price = 0
        for i in range(0, math.ceil(max_item_num / 100)):
            if request_min_price == now_price * 100:
                now_price += 1
            request_min_price = math.floor(now_price * 100)
            for page in range(1, 11):
                self.logger.info(f'request count={i * 10 + page}, min_price={request_min_price}, item_page={page}')
                products = amazon_api.search_products(
                    browse_node=node,
                    item_page=page,
                    min_price=request_min_price,
                    sort_by='Price:LowToHigh'
                )
                if products is None:
                    self.logger.info(f'response products={products}')
                    break
                self.logger.info(f'response products={len(products)}')
                for p in products:
                    pp = ProductWrapper(p)
                    if pp.predict_filtered() == False:
                        product_set.add(pp)
                    now_price = pp.price_value
            else:
                continue
            break
        return product_set

    def out_product_set(self, product_set, outfile):
        with open(outfile, 'w', encoding='utf-8') as out:
            out.write('author,series_title,title,price,url,genles\n')
            for x in sorted(product_set):
                out.write(f'"{x.author}","{x.series_title}","{x.title}","{x.price_display}","{x.url}","{x.genles}"\n')

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version="%(prog)s (version {version})".format(version=__version__))
    parser.add_argument("arg1", help='Amazon Node')
    args = parser.parse_args()
    Main().main(args)
