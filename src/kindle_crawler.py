import math

import logzero
from amazon.paapi import AmazonAPI

import kindle_product
import settings


class KindleCrawler:
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
                    kindle_products = [
                        kindle_product.from_response(p) for p in products]
                    for p in kindle_products:
                        now_price = max(now_price, p.price_value)
                        product_set.add(p)
                    # 次のアイテムが取得できない見込みなら終了
                    if len(products) < 10:
                        break
            else:
                continue
            break
        return product_set
