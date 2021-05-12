#!/usr/bin/env python3
__version__ = "0.1.0"

import argparse
import logzero
import settings
import xml.etree.ElementTree as etree
import pandas

class KindleLibExporter:
    def __init__(self):
        logzero.logfile(
            settings.settings_dict['logfile'],
            loglevel=20,
            maxBytes=1e6,
            backupCount=3
        )
        self.logger = logzero.logger

    def main(self, args):
        self.logger.info(args)
        self.logger.info(f'import {settings.kindle_xml}')

        all_record =[]
        record = {}
        for event, el in etree.iterparse(settings.kindle_xml):
            if event == 'end' and el.tag in ['ASIN','title','publication_date']:
                record[el.tag] = el.text
            elif event == 'end' and el.tag in ['author','publisher']:
                if el.tag in record:
                    record[el.tag] = record[el.tag] + ',' + el.text
                else:
                    record[el.tag] = el.text
            elif event == 'end' and el.tag == 'meta_data':
                all_record.append(record)
                record = {}

        df = pandas.DataFrame(all_record)
        df.sort_values('title', inplace=True)
        df.to_csv(settings.kindle_lib, index=False, encoding='UTF-8', sep='\t')

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version=f'version {__version__})')
    args = parser.parse_args()
    KindleLibExporter().main(args)
