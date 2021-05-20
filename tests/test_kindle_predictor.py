import kindle_product
import kindle_predictor
import logzero

logzero.logfile(
    '../log/test.log', loglevel=20,
    maxBytes=1e6, backupCount=3
)
log = logzero.logger

def test_a():
    kindle= kindle_product.KindleProduct()
    kindle.title = 'aaa'
    kindle.asin = 'B009GXMCIU'
    kindle.genles = ['ティーンズラブ','ライトノベル']
    kindle.is_adult = False
    kindle.authors = ['与沢 翼']

    cause_dict = kindle_predictor.scoring(kindle)
    log.info(cause_dict)

    s = kindle_predictor.agg_score(cause_dict)
    log.info(s)

def test_b():
    kindle= kindle_product.KindleProduct()
    kindle.title = '100円のコーラを1000円で売る方法3'
    kindle.asin = 'B009GXMCIUX'

    log.info(kindle_predictor.is_one_in_series(kindle))
