#!/usr/bin/env python3
__version__ = "0.1.0"

import argparse
import logzero
import settings
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
        amazon_api = AmazonAPI(settings.amazon_access_key, settings.amazon_secret_key, settings.amazon_assosiate_id, 'JP')
        with open(settings.outfile, 'w', encoding='utf-8') as out:
            out.write('title,price,url\n')
            result = []
            now_price = 1
            for i in range(0, 2):
                min_price = now_price * 100
                for i in range(1, 11):
                    self.logger.info(f"browse_node='3550442051',item_count=10, item_page={i}, min_price={min_price}")
                    products = amazon_api.search_products(browse_node='3550442051',item_count=10, item_page=i, items_per_page=10, min_price=min_price, sort_by='Price:LowToHigh')
                    if products is None:
                        break
                    for x in products:
                        if len(list(filter(lambda y: y.title == x.title, result))) == 0:
                            self.logger.info(f'{x.title}')
                            result.append(x)
                        now_price = x.prices.price.value
            for x in sorted(result, key=lambda p : p.title):
                out.write(f'{x.title},{x.prices.price.value},{x.url}\n')

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version="%(prog)s (version {version})".format(version=__version__))
    args = parser.parse_args()
    Main().main(args)
