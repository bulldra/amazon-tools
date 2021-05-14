#!/usr/bin/env python3
__version__ = "0.1.0"

import re

def tlanslate_series_title(title):
    title = all_remove(title)
    title = choice_remove(title)
    return title

def all_remove(title):
    bracket_word_list =[
        r'雑誌',
        r'部分販売',
        r'マップ編',
        r'合本版',
        r'極！合本シリーズ',
        r'増補改訂版',
        r'カラー版',
        r'モノクロ版',
        r'新版',
        r'完全版',
        r'書き下ろしイラスト付',
        r'図解',
        r'.*描き下ろし特典付',
        r'完',
        r'ファンタジア文庫',
        r'フルカラー',
        r'マンガ',
        r'合本版',
        r'電子特別版',
        r'電子版',
        r'小説',
        r'編集版',
        r'電子版限定！　豪華特典レシピつき',
        r'新訂版',
        r'前編',
        r'後編',
        r'分割版',
        r'新訳版',
        r'ワイド版',
    ]
    space_word_list = [
        r'通常版',
        r'完全版',
        r'カラー版',
        r'モノクロ版',
    ]

    regex_list =[r'\s*[\[［〔【\(（]' + x + r'[】〕\]\)）］]\s*' for x in bracket_word_list]
    regex_list += [r'\s*' + x + r'\s*' for x in space_word_list]

    for r in regex_list:
        title = re.sub(r,'',title, flags=re.IGNORECASE)
    return title

def choice_remove(title):
    keyword = r'\d一二三四五六七八九十IⅤＩXⅠⅡ上中下全'

    regex_list =[
        (r'([\s\d]+年)*\s*[\d]+月号\s*',''),
        (r'\s*[VＶ][OＯ][LＬ．][\.．]\s*[\d]+\s*',''),
        (r'\s*[ＮN][OＯ][\.．]\s*[\d]+\s*',''),
        (r'\s*―*[第全]*[' + keyword + ']+巻―*\s*',''),
        (r'\s*\([' + keyword + r']\)\s*',''),
        (r'\s*（[' + keyword + r']+）\s*',''),
        (r'\s*＜[' + keyword + r']+＞\s*',''),
        (r'[：\s]+[' + keyword + r']+\s+',''),
        (r'([^' + keyword + r'+])[' + keyword + r']+\s\(','\\1('),
        (r'[：\s]*[' + keyword + ']+$',''),
        (r'\s+\(','('),
    ]

    for r in regex_list:
        result = re.sub(r[0], r[1], title, flags=re.IGNORECASE)
        if title != result:
            return result

    return title
