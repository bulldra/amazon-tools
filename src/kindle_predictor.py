#!/usr/bin/env python3

__version__ = "0.1.0"

import os

import pandas

import kindle_util
import settings


class KindlePredicotr:
    def __init__(self):
        if os.path.isfile(settings.kindle_lib):
            self.lib = pandas.read_csv(settings.kindle_lib, sep="\t")
        else:
            dict = {"series_title": [], "asin": []}
            self.lib = pandas.DataFrame(data=dict)

    def scoring_value(self, kindle):
        return self.agg_score(self.scoring(kindle))

    def scoring(self, kindle):
        cause_dict = {}
        if (self.lib["asin"] == kindle.asin).sum() > 0:
            cause_dict["having"] = settings.model_having
        else:
            cause_dict["having"] = 0
        cause_dict["adult"] = settings.model_adult if kindle.is_adult else 0
        cause_dict["genle"] = self._scoring_element_match(
            settings.genle_black_list, kindle.genles
        )
        cause_dict["author"] = self._scoring_element_match(
            settings.author_black_list, kindle.authors
        )
        cause_dict["title"] = self._scoring_part_match(
            settings.title_black_list, [kindle.title])
        cause_dict["series"] = -1 if self._is_one_in_series(kindle) else 0
        return cause_dict

    def agg_score(self, cause_dict):
        score = 0.0
        for v in cause_dict.values():
            score += self.agg_score(v) if type(v) is dict else v
        return score

    def _scoring_element_match(self, model, elem):
        score = {}
        if type(elem) is list and type(model) is dict:
            for e in elem:
                if type(e) is list:
                    score.update(self._scoring_element_match(model, e))
                else:
                    for k, v in model.items():
                        if k in elem:
                            score[k] = max(score.get(k, 0), v)
        return score

    def _scoring_part_match(self, model, elem):
        score = {}
        if type(elem) is list and type(model) is dict:
            for k, v in model.items():
                for e in elem:
                    if k in e:
                        score[k] = score.get(k, 0) + v
        return score

    def _is_one_in_series(self, kindle):
        series_title = kindle_util.norm_series_title(kindle.title)
        return (
            (self.lib["asin"] != kindle.asin) & (
                self.lib["series_title"] == series_title)
        ).sum() > 0
