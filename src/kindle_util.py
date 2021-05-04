import re

def tlanslate_series_title(title):
    title = all_remove(title)
    title = choice_remove(title)
    return title

def all_remove(title):
    regex_list =[
        '\\s*[\\[【〔].+?[\\]】〕]\\s*',
        '\\s*(完全|通常)版\\s*'
    ]

    for r in regex_list:
        title = re.sub(r,'',title)
    return title

def choice_remove(title):
    regex_list =[
        '([\\s0-9０-９]+年)*\\s*[0-9０-９]+月[号\\s]*',
        '[\\s＜（\\(第：]+([VvＶｖ][OoＯｏ][LlＬｌ．][\\.．])*([NnＮn][OoＯｏ][\\.．])*[0-9０-９一二三四五六七八九十IⅤＩX上中下]+[巻\\s\\)）＞]*',
        '[第：]*[0-9０-９一二三四五六七八九IⅤＩX]+[巻\\s]+',
        '[第：]*[0-9０-９一二三四五六七八九IⅤＩX]+[巻\\s]*$'
    ]

    for r in regex_list:
        result = re.sub(r,'',title)
        if title != result:
            return result
    return title
