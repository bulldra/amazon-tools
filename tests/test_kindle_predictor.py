#!/usr/bin/env python3

__version__ = "0.1.0"

import kindle_predictor
import kindle_product
import settings


def test_scoring_black1():
    kindle = kindle_product.KindleProduct()
    predictor = kindle_predictor.KindlePredicotr()

    kindle.title = "aaa"
    kindle.asin = "B00XWZR08B"
    kindle.genles = [["ティーンズラブ", "ライトノベル"]]
    kindle.is_adult = False
    kindle.authors = ["与沢翼"]

    cause_dict = predictor.scoring(kindle)
    assert cause_dict == {
        "adult": 0,
        "author": {"与沢翼": 2},
        "genle": {"ティーンズラブ": 4},
        "having": 0,
        "series": 0,
        "title": {},
    }

    score = predictor.scoring_value(kindle)
    assert score == 6


def test_scoring_black2():
    kindle = kindle_product.KindleProduct()
    predictor = kindle_predictor.KindlePredicotr()

    kindle.title = "aaa"
    kindle.asin = "ZZZZZ"
    kindle.genles = [
        ["本", "ジャンル別", "コミック・ラノベ・BL", "コミック"],
        ["Kindleストア", "カテゴリー別", "Kindle本", "マンガ"],
    ]
    kindle.is_adult = False
    kindle.authors = ["川上量生"]

    cause_dict = predictor.scoring(kindle)
    assert cause_dict == {
        "adult": 0,
        "author": {},
        "genle": {},
        "having": 0,
        "series": 0,
        "title": {},
    }

    score = predictor.scoring_value(kindle)
    assert score == 0


def test_scoring_genls():
    kindle = kindle_product.KindleProduct()
    predictor = kindle_predictor.KindlePredicotr()

    kindle.title = "aaa"
    kindle.asin = "B00XWZR08A"
    kindle.genles = [
        ["本", "ジャンル別", "コミック・ラノベ・BL", "コミック"],
        ["Kindleストア", "カテゴリー別", "Kindle本", "マンガ"],
    ]
    kindle.is_adult = False
    kindle.authors = ["川上量生"]
    score = predictor._scoring_element_match(
        settings.genle_black_list, kindle.genles
    )
    assert score == {}
