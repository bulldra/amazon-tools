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
        title = re.sub(r,'',title)
    return title

def choice_remove(title):
    regex_list =[
        r'([\s\d]+年)*\s*[\d]+月号\s*',
        r'\s*[VvＶｖ][OoＯｏ][LlＬｌ．][\.．]\s*[\d]+\s*',
        r'\s*[ＮNｎn][OoＯｏ][\.．]\s*[\d]+\s*',
        r'[：\s]*[\d一二三四五六七八九十IⅤＩX上中下]+\s+',
        r'\s*\([上中下全\d一二三四五六七八九十IⅤＩX]+\)\s*',
        r'\s*（[上中下\d一二三四五六七八九十IⅤＩX]+）\s*',
        r'\s*＜[上中下\d一二三四五六七八九十IⅤＩX]+＞\s*',
        r'\s*―*[第全]*[\d一二三四五六七八九十IⅤＩⅠX]+巻―*\s*',
        r'\s*[\d一二三四五六七八九IⅤＩⅠⅡX]+\s*$',
    ]

    for r in regex_list:
        result = re.sub(r, '', title)
        if title != result:
            return result

    title = re.sub(r'\s+(\()','(',title)
    return title
