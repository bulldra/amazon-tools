#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import re

def norm_autohr(atutor):
    return re.sub(r'\s+','', atutor)

def norm_series_title(title):
    word_list =[
        r'雑誌', r'部分販売', r'マップ編', r'合本版', r'極！合本シリーズ', r'増補改訂版',
        r'カラー版', r'モノクロ版', r'新版', r'完全版', r'通常版', r'書き下ろしイラスト付',
        r'図解', r'描き下ろし特典付', r'完', r'ファンタジア文庫', r'フルカラー',
        r'マンガ', r'合本版', r'電子特別版', r'電子版', r'小説', r'編集版',
        r'電子版限定！　豪華特典レシピつき', r'新訂版', r'前編', r'後編', r'分割版',
        r'新訳版', r'ワイド版', r'イラスト特典付', r'電子版限定特典付き', r'限定特典付き',
        r'単話版',
    ]
    regex_list = [(r'\s*[\[［〔【\(（]\s*' + x + r'\s*[\s】〕\]\)）］]\s*',) for x in word_list]
    regex_list += [(r'\s*' + x + r'\s*',) for x in word_list]

    keyword = r'\d一二三四五六七八九十IⅤＩXⅠⅡ上中下全'
    regex_list += [
        (r'([\s\d]+年)*\s*[\d]+月号\s*',),
        (r'\s*[VＶ][OＯ][LＬ．][\.．]\s*[\d]+\s*',),
        (r'\s*[ＮN][OＯ][\.．]\s*[\d]+\s*',),
        (r'\s*―*[第全]*[' + keyword + r']+巻[―\s]*',),
        (r'\s*\([' + keyword + r']+\)\s*',),
        (r'\s*（[' + keyword + r']+）\s*',),
        (r'\s*＜[' + keyword + r']+＞\s*',),
        (r'[：:\s]+[' + keyword + r']+\s+',),
        (r'([^' + keyword + r']+)[' + keyword + r']+\s\(', r'\1('),
        (r'([^' + keyword + r'：:\s]+)[：:\s]*[' + keyword + r']+$', r'\1'),
        (r'([^' + keyword + r'：:\s]+)[：:\s]*[' + keyword + r']+\(', r'\1('),
        (r'\s+\(',r'('),
    ]

    for r in regex_list:
        s = r[1] if len(r) == 2 else ''
        title = re.sub(r[0], s, title, flags=re.IGNORECASE)

    return title
