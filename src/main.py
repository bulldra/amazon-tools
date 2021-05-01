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
        amazon_api = AmazonAPI(settings.amazon_access_key, settings.amazon_secret_key, settings.amazon_assosiate_id, 'JP')
        with open(settings.outfile, 'w', encoding='utf-8') as out:
            out.write('author,title,price,url\n')
            result = set()
            now_price = 1
            for i in range(0, 3):
                min_price = now_price * 100
                for i in range(1, 11):
                    self.logger.info(f"request browse_node='{settings.monthly_node}', item_count=10, item_page={i}, min_price={min_price}, sort_by='Price:LowToHigh'")
                    products = amazon_api.search_products(browse_node=settings.monthly_node,item_count=10, item_page=i, items_per_page=10, min_price=min_price, sort_by='Price:LowToHigh')
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

            for x in filter(lambda x : x.is_adult == False and x.author not in settings.author_black_list, sorted(result)):
                out.write(f'"{x.author}","{x.title}","{x.price_display}","{x.url}"\n')

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version="%(prog)s (version {version})".format(version=__version__))
    args = parser.parse_args()
    Main().main(args)
