#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import os
import json

def load_json(path):
    with open(_build_path(path), 'r') as conf:
        return json.load(conf)

def _build_path(path):
    abspath = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    abspath = os.path.abspath(abspath)
    if os.path.exists(abspath):
        return abspath
    else:
        raise FileNotFoundError(abspath)

settings_dict = load_json('../config/settings.json')
secrets_dict = load_json('../config/secrets.json')
model_dict = load_json('../config/model.json')

amazon_access_key = secrets_dict['amazon_access_key']
amazon_secret_key = secrets_dict['amazon_secret_key']
amazon_assosiate_id = secrets_dict['amazon_assosiate_id']

kindle_lib = settings_dict['kindle_lib']
kindle_xml = settings_dict['kindle_xml']

outfile = settings_dict['outfile']
max_item_num = settings_dict['max_item_num']
min_price = settings_dict['min_price']

author_black_list = model_dict['author_black_list']
genle_black_list = model_dict['genle_black_list']
title_black_list = model_dict['title_black_list']
