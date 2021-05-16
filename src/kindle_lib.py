#!/usr/bin/env python3
__version__ = "0.1.0"

import argparse
import logzero
import settings
import xml.etree.ElementTree as etree
import pandas
import kindle_util
import sys

class KindleLibExporter:
    def __init__(self):
        logzero.logfile(
            settings.settings_dict['logfile'],
            loglevel=20, maxBytes=1e6, backupCount=3
        )
        self.logger = logzero.logger

    def import_kindle_xml(self, kindle_xml):
        matrix =[]
        record = {}
        for event, el in etree.iterparse(kindle_xml):
            if event == 'end':
                if el.tag == 'title':
                    record[el.tag] = el.text
                    record['series_title'] = kindle_util.tlanslate_series_title(el.text)
                elif el.tag == 'ASIN':
                    record['asin'] = el.text
                    record['url'] = f'https://www.amazon.co.jp/dp/{el.text}'
                elif el.tag in ['author', 'publisher']:
                    if el.tag in record:
                        record[el.tag] = f'{record[el.tag]},{el.text}'
                    else:
                        record[el.tag] = el.text
                elif el.tag in ['publication_date']:
                    record[el.tag] = el.text
                elif el.tag == 'meta_data':
                    matrix.append(record)
                    record = {}
        return matrix

    def main(self, args):
        self.logger.info(args)

        ## 指定されたファイルパスのXMLを解析
        self.logger.info(f'import {args.arg1}')
        df = pandas.DataFrame(self.import_kindle_xml(args.arg1))
        df.sort_values(['series_title','title'], inplace=True)

        ## ファイルパスが指定されていればファイルに出力、そうでないなら sys.out に出力
        out = sys.stdout if args.out is None else args.out
        self.logger.info(f'export {out}')
        df.to_csv(out, index=False, encoding='UTF-8', sep='\t')

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version=f'version {__version__}')
    parser.add_argument('arg1', help='import file', default=settings.kindle_xml)
    parser.add_argument('-o','--out', help='output file')
    args = parser.parse_args()
    KindleLibExporter().main(args)
