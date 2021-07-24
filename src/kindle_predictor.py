#!/usr/bin/env python3

__version__ = "0.1.0"

import pandas

import kindle_util
import settings

lib = pandas.read_csv(settings.kindle_lib, sep="\t")


def scoring_value(kindle):
    return agg_score(scoring(kindle))


def scoring(kindle):
    cause_dict = {}
    cause_dict["having"] = 1 if (lib["asin"] == kindle.asin).sum() > 0 else 0
    cause_dict["adult"] = 0.2 if kindle.is_adult else 0
    cause_dict["genle"] = _scoring_element_match(
        settings.genle_black_list, kindle.genles
    )
    cause_dict["author"] = _scoring_element_match(
        settings.author_black_list, kindle.authors
    )
    cause_dict["title"] = _scoring_part_match(settings.title_black_list, [kindle.title])
    cause_dict["series"] = -1 if _is_one_in_series(kindle) else 0
    return cause_dict


def agg_score(cause_dict):
    score = 0.0
    for v in cause_dict.values():
        score += agg_score(v) if type(v) is dict else v
    return score


def _scoring_element_match(model, elem):
    score = {}
    if type(elem) is list and type(model) is dict:
        for e in elem:
            if type(e) is list:
                score.update(_scoring_element_match(model, e))
            else:
                for k, v in model.items():
                    if k in elem:
                        score[k] = max(score.get(k, 0), v)
    return score


def _scoring_part_match(model, elem):
    score = {}
    if type(elem) is list and type(model) is dict:
        for k, v in model.items():
            for e in elem:
                if k in e:
                    score[k] = score.get(k, 0) + v
    return score


def _is_one_in_series(kindle):
    series_title = kindle_util.norm_series_title(kindle.title)
    return (
        (lib["asin"] != kindle.asin) & (lib["series_title"] == series_title)
    ).sum() > 0
