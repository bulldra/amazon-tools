#!/usr/bin/env python3

__version__ = "0.1.0"

import argparse
import math

import logzero
from amazon.paapi import AmazonAPI

import kindle_predictor
import settings
from kindle_product import KindleProduct


class Main:
    def __init__(self):
        logzero.logfile(
            settings.settings_dict["logfile"], loglevel=20, maxBytes=1e6, backupCount=3
        )
        self.logger = logzero.logger

    def crawl_product_set(self, node, max_item_num, min_price):
        amazon_api = AmazonAPI(
            settings.amazon_access_key,
            settings.amazon_secret_key,
            settings.amazon_assosiate_id,
            "JP",
        )
        product_set = set()
        now_price = min_price
        request_min_price = 0

        # PAAPIv5は10アイテムを最大10回リクエスト
        # 必要なアイテム数 / (10 * 10) 回以上のリクエストセットが必要
        request_set_num = math.ceil(max_item_num / (10 * 10))
        self.logger.info(f"response products={request_set_num}")
        for i in range(request_set_num):
            # 100アイテム取得して価格が変わらない場合にはループを防ぐため+1円する
            if request_min_price == now_price * 100:
                now_price += 1
            # PAAPIv5の仕様で日本円のリクエストは100倍する必要がある
            request_min_price = math.floor(now_price * 100)

            # 10回リクエスト
            for page in range(1, 11):
                self.logger.info(
                    f"request node={node}, count={i * 10 + page}, \
min_price={request_min_price}, item_page={page}"
                )
                products = amazon_api.search_products(
                    browse_node=node,
                    item_page=page,
                    min_price=request_min_price,
                    sort_by="Price:LowToHigh",
                )

                # 次のアイテムが取得できないなら終了
                if products is None:
                    self.logger.info(f"response products={products}")
                    break
                else:
                    self.logger.info(f"response products={len(products)}")
                    kindle_products = [KindleProduct(p) for p in products]
                    for p in kindle_products:
                        now_price = max(now_price, p.price_value)
                        v = kindle_predictor.scoring_value(p)
                        if v < 0.3:
                            product_set.add(p)
                        else:
                            s = kindle_predictor.scoring(p)
                            self.logger.info(f"remove {p.title} {v} {s}")
                    # 次のアイテムが取得できない見込みなら終了
                    if len(products) < 10:
                        break
            else:
                continue
            break
        return product_set

    def out_product_set(self, product_set, outfile):
        with open(outfile, "w", encoding="utf-8") as out:
            out.write("author,title,price,url,genles\n")
            for x in sorted(product_set):
                out.write(
                    f'"{x.author}","{x.title}","{x.price_display}","{x.url}","{x.genles}"\n'
                )

    def main(self, args):
        self.logger.info(f"{args}")
        product_set = self.crawl_product_set(
            args.arg1, settings.max_item_num, int(args.min_price)
        )
        self.out_product_set(product_set, settings.outfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version=f"{__version__}")
    parser.add_argument("arg1", help="Amazon Node")
    parser.add_argument(
        "--min_price", help="Min Price", default=str(settings.min_price)
    )
    args = parser.parse_args()
    Main().main(args)
