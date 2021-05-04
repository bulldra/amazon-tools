import re

def tlanslate_series_title(title):
    title = all_remove(title)
    title = choice_remove(title)
    return title

def all_remove(title):

    regex_list =[
        '\\s*[\\[〔【\\(]*(雑誌|部分販売|マップ編|極！合本シリーズ|増補改訂版|合本版|書き下ろしイラスト付|完全版|通常版|モノクロ版|カラー版|Amazon.co.jp限定描き下ろし特典付)[】〕\\]\\)]*\\s*',
        '（完）'
    ]

    for r in regex_list:
        title = re.sub(r,'',title)
    return title

def choice_remove(title):
    regex_list =[
        '([\\s0-9０-９]+年)*\\s*[0-9０-９]+月号\\s*',
        '\\s*[VvＶｖ][OoＯｏ][LlＬｌ．][\\.．]\\s*[0-9０-９]+\\s*',
        '\\s*[ＮNｎn][OoＯｏ][\\.．]\\s*[0-9０-９]+\\s*',
        '[：\\s]*[0-9０-９一二三四五六七八九十IⅤＩX上中下]+\\s+',
        '\\s*\\([上中下全0-9０-９一二三四五六七八九十IⅤＩX]+\\)\\s*',
        '\\s*＜[上中下0-9０-９一二三四五六七八九十IⅤＩX]+＞\\s*',
        '\\s*（[上中下0-9０-９一二三四五六七八九十IⅤＩX]+）\\s*',
        '\\s*―*[第全]*[0-9０-９一二三四五六七八九十IⅤＩX]+巻―*\\s*',
        '\\s*[0-9０-９一二三四五六七八九IⅤＩX]+$',
    ]

    for r in regex_list:
        result = re.sub(r, '', title)
        if title != result:
            return result

    title = re.sub('\\s+(\\()','(',title)
    return title
