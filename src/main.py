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
        products = amazon_api.search_products(item_count=25, keywords='python')
        for x in products:
            print(f'{x.title}\t{x.url}')

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version="%(prog)s (version {version})".format(version=__version__))
#    parser.add_argument("args1")
    args = parser.parse_args()
    Main().main(args)
