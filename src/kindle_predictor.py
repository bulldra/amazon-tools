#!/usr/bin/env python3
__version__ = "0.1.0"

import settings

def scoring(kindle):
    cause_dict = {}
    cause_dict['having'] = 1 if kindle.asin in settings.kindle_lib_list else 0
    cause_dict['adult'] = 0.2 if kindle.is_adult else 0
    cause_dict['genle'] = _scoring_element_match(settings.genle_black_list, kindle.genles)
    cause_dict['author'] = _scoring_element_match(settings.author_black_list, kindle.authors)
    cause_dict['title'] = _scoring_part_match(settings.title_black_list, [kindle.title])

    return cause_dict

def agg_score(cause_dict):
    score = 0.0
    for v in cause_dict.values():
        if type(v) is dict:
            score += agg_score(v)
        else:
            score += v
    return score

def _scoring_element_match(model, elem):
    score = {}
    if type(elem) is list and type(model) is dict:
        for k, v in model.items():
            if k in elem:
                score[k] = score.get(k, 0) + v
    return score

def _scoring_part_match(model, elem):
    score = {}
    if type(elem) is list and type(model) is dict:
        for k, v in model.items():
            for e in elem:
                if k in e:
                    score[k] = score.get(k, 0) + v
    return score
