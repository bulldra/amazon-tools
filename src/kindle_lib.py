#!/usr/bin/env python3

__version__ = "0.1.0"

import argparse
import sys
import xml.etree.ElementTree as etree

import logzero
import pandas

import kindle_util
import settings


class KindleLibExporter:
    def __init__(self):
        logzero.logfile(
            settings.settings_dict["logfile"], loglevel=20, maxBytes=1e6, backupCount=3
        )
        self.logger = logzero.logger

    def import_kindle_xml(self, kindle_xml):
        matrix = []
        rec = {}
        for event, el in etree.iterparse(kindle_xml, events=["start", "end"]):
            if event == "start" and el.tag == "meta_data":
                rec = {}
            elif event == "end":
                if el.tag == "title":
                    rec[el.tag] = el.text
                    rec["series_title"] = kindle_util.norm_series_title(el.text)
                elif el.tag == "ASIN":
                    rec["asin"] = el.text
                    rec["url"] = f"https://www.amazon.co.jp/dp/{el.text}"
                elif el.tag in ["author", "publisher"]:
                    e = kindle_util.norm_autohr(el.text)
                    rec[el.tag] = f"{rec[el.tag]},{e}" if el.tag in rec else e
                elif el.tag in ["publication_date"]:
                    rec[el.tag] = el.text
                elif el.tag == "meta_data":
                    if rec["title"] == "---------------":
                        continue
                    rec.setdefault("author", "著者情報なし")
                    matrix.append(rec)
        return matrix

    def main(self, args):
        self.logger.info(args)

        # 指定されたファイルパスのXMLを解析
        self.logger.info(f"import {args.arg1}")

        # 結果を整形
        df = pandas.DataFrame(self.import_kindle_xml(args.arg1))
        df = df.sort_values(["author", "series_title", "title"])
        df = df.reindex()

        # ファイルパスが指定されていればファイルに出力、そうでないなら sys.stdout に出力
        out = sys.stdout if args.out is None else args.out
        self.logger.info(f"export {out}")
        df.to_csv(out, index=False, encoding="UTF-8", sep="\t")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version=f"version {__version__}")
    parser.add_argument("arg1", help="import file", default=settings.kindle_xml)
    parser.add_argument("-o", "--out", help="output file")
    KindleLibExporter().main(parser.parse_args())
