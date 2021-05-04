import re

def tlanslate_series_title(title):
    title = first_remove(title)
    title = second_remove(title)
    return title

def first_remove(title):
    title = re.sub('\\s*[\\[【〔].+?[\\]】〕]\\s*','',title)
    title = re.sub('\\s*(完全|通常)版\\s*','',title)
    return title

def second_remove(title):
    result = re.sub('([\\s0-9０-９]+年)*\\s*[0-9０-９]+月[号\\s]*','',title)
    if title != result:
        return result

    result = re.sub('[\\s＜（\\(第：]+([VvＶｖ][OoＯｏ][LlＬｌ．][\\.．])*([NnＮn][OoＯｏ][\\.．])*[0-9０-９一二三四五六七八九十IⅤＩX上中下]+[巻\\s\\)）＞]*', '', title)
    if title != result:
        return result

    result = re.sub('[第：]*[0-9０-９一二三四五六七八九IⅤＩX]+[巻\\s]+','',title)
    if title != result:
        return result

    result = re.sub('[第：]*[0-9０-９一二三四五六七八九IⅤＩX]+[巻\\s]*$','',title)
    if title != result:
        return result

    return result
