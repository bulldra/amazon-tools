import re

def tlanslate_series_title(title):
    title = all_remove(title)
    title = choice_remove(title)
    return title

def all_remove(title):
    regex_list =[
        '\\s*[\\[【〔].+?[\\]】〕]\\s*',
        '\\s*(完全|通常|モノクロ|カラー)版\\s*'
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
