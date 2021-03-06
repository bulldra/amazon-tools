#!/usr/bin/env python3

__version__ = "0.1.0"

import argparse
import os
import pickle

import logzero

import kindle_crawler
import kindle_predictor
import settings


class Main:
    def __init__(self):
        logzero.logfile(
            settings.settings_dict["logfile"], loglevel=20, maxBytes=1e6, backupCount=3
        )
        self.logger = logzero.logger
        self.predictor = kindle_predictor.KindlePredicotr()

    def out_product_set(self, product_set, outfile):
        with open(outfile, "w", encoding="utf-8") as out:
            out.write("asin,author,title,price,url,genles\n")
            for x in sorted(product_set):
                out.write(
                    f'"{x.asin}","{x.author}","{x.title}","{x.price_display}","{x.url}","{x.genles}"\n'
                )

    def predict(self, product_set):
        new_product_set = set()
        for p in product_set:
            v = self.predictor.scoring_value(p)
            if v < 0.3:
                new_product_set.add(p)
            else:
                s = self.predictor.scoring(p)
                self.logger.info(f"remove {p.title} {v} {s}")
        return new_product_set

    def main(self, args):
        self.logger.info(f"{args}")

        product_set = None
        tmp_outpath = settings.tmp_outfile.format(args.arg1)
        if not os.path.isfile(tmp_outpath):
            product_set = kindle_crawler.KindleCrawler().crawl_product_set(
                args.arg1, settings.max_item_num, int(args.min_price)
            )
            with open(tmp_outpath, 'wb') as f:
                pickle.dump(product_set, f)
        else:
            with open(tmp_outpath, 'rb') as f:
                product_set = pickle.load(f)

        product_set = self.predict(product_set)
        self.out_product_set(product_set, settings.outfile.format(args.arg1))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version",
                        version=f"{__version__}")
    parser.add_argument("arg1", help="Amazon Node")
    parser.add_argument(
        "--min_price", help="Min Price", default=str(settings.min_price)
    )
    args = parser.parse_args()
    Main().main(args)
