#!/usr/bin/env python3
__version__ = "0.1.0"

import kindle_util

def test_sereis_title():
    except_list =[
        ['～一攫千金!～ 1 (B\'s-LOG COMICS)','～一攫千金!～(B\'s-LOG COMICS)'],
        ['0能者ミナト＜2＞', '0能者ミナト'],
        ['100億円稼ぐ人の思考法(あさ出版電子書籍)','100億円稼ぐ人の思考法(あさ出版電子書籍)'],
        ['ANGELIC LAYER(1) (角川コミックス・エース)','ANGELIC LAYER(角川コミックス・エース)'],
        ['31歳、初カレ。 1巻 (G☆Girls)','31歳、初カレ。(G☆Girls)'],
        ['31歳、初カレ。1巻 (G☆Girls)','31歳、初カレ。(G☆Girls)'],
        ['BOYS BE…シリーズ1巻','BOYS BE…シリーズ'],
        ['回顧録（１） (コンパスコミックス)','回顧録(コンパスコミックス)'],
        ['Ladies Collection vol.004 (KAZUP編集部)','Ladies Collection(KAZUP編集部)'],
        ['【部分販売】真・女神転生ガイド　【マップ編】 (アトラスファミ通)','真・女神転生ガイド(アトラスファミ通)'],
        ['【極！合本シリーズ】 いかさま博覧亭シリーズ2巻','いかさま博覧亭シリーズ'],
        ['江戸の男女の色恋ばなし傑作選　第四巻 (蜜麻呂)','江戸の男女の色恋ばなし傑作選(蜜麻呂)'],
        ['ネオン蝶1','ネオン蝶'],
        ['ワンダーフォーゲル 2020年 10月号 [雑誌]','ワンダーフォーゲル'],
        ['ワンダーフォーゲル 10月号 [雑誌]','ワンダーフォーゲル'],
        ['ソトコト2018年 12月号 [雑誌]','ソトコト'],
        ['〔増補改訂版〕会話帳 【カタコト会話帳シリーズ】','会話帳'],
        ['どうぶつの国 完全版（10）','どうぶつの国'],
        ['バッファロー５人娘　通常版','バッファロー５人娘'],
        ['出雲のあやかしホテルに就職します ： 2 (双葉文庫)','出雲のあやかしホテルに就職します(双葉文庫)'],
        ['新書太閤記（十一） (吉川英治歴史時代文庫)','新書太閤記(吉川英治歴史時代文庫)'],
        ['最新ゲーム攻略ガイド VOL.6 2021 ～ネ','最新ゲーム攻略ガイド2021 ～ネ'],
        ['ＤｅＬｉ　ｍａｇａｚｉｎｅ　ｖｏｌ．０１ 主婦の友生活シリーズ','ＤｅＬｉ　ｍａｇａｚｉｎｅ主婦の友生活シリーズ'],
        ['ＰＬＵＳ１　Ｌｉｖｉｎｇ　Ｎｏ．８３','ＰＬＵＳ１　Ｌｉｖｉｎｇ'],
        ['狼と香辛料XIII　Side Colors III (電撃文庫)','狼と香辛料Side Colors(電撃文庫)'],
        ['方法2 (中経出版)','方法(中経出版)'],
        ['100円のコーラを1000円で売る方法 (中経出版)','100円のコーラを1000円で売る方法(中経出版)'],
        ['10年戦えるデータ分析入門 (Informatics ＆IDEA)','10年戦えるデータ分析入門(Informatics ＆IDEA)'],
        ['3月のライオン 1 (ジェッツコミックス)','3月のライオン(ジェッツコミックス)'],
        ['HUNTER×HUNTER モノクロ版 4 (ジャンプコミックスDIGITAL)','HUNTER×HUNTER(ジャンプコミックスDIGITAL)'],
        ['【合本版】オイレンシュピーゲル　全４巻 (角川スニーカー文庫)','オイレンシュピーゲル(角川スニーカー文庫)']
    ]

    for a in except_list:
        assert kindle_util.tlanslate_series_title(a[0]) == a[1]

def test_ser():
    titles =[]
    with open('../work/kindle_lib_title.txt', 'r') as conf:
        for line in conf.read().splitlines():
            titles.append(line)

    with open('../work/kindle_lib_title_a.txt', 'w') as out:
        out.write('title,result,is_match\n')
        for x in titles:
            a = kindle_util.tlanslate_series_title(x)
            out.write(f'{x},{a},{x==a}\n')
