#!/usr/bin/env python3
__version__ = "0.1.0"

import re

def tlanslate_series_title(title):
    title = all_remove(title)
    title = choice_remove(title)
    return title

def all_remove(title):

    regex_list =[
        r'\s*[\[〔【\(]*(雑誌|部分販売|マップ編|極！合本シリーズ|増補改訂版|合本版|書き下ろしイラスト付|完全版|通常版|モノクロ版|カラー版|Amazon.co.jp限定描き下ろし特典付)[】〕\]\)]*\s*',
        r'（完）'
    ]

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
        r'\s*＜[上中下\d一二三四五六七八九十IⅤＩX]+＞\s*',
        r'\s*（[上中下\d一二三四五六七八九十IⅤＩX]+）\s*',
        r'\s*―*[第全]*[\d一二三四五六七八九十IⅤＩX]+巻―*\s*',
        r'\s*[\d一二三四五六七八九IⅤＩX]+$',
    ]

    for r in regex_list:
        result = re.sub(r, '', title)
        if title != result:
            return result

    title = re.sub(r'\s+(\()','(',title)
    return title
