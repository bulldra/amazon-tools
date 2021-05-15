#!/usr/bin/env python3
__version__ = "0.1.0"

import os
import json

def load_json_setting(path):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    if os.path.exists(path):
        with open(path, 'r') as conf:
            return json.load(conf)
    else:
        return None

def load_text_list(path):
    result = []
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    if os.path.exists(path):
        with open(path, 'r') as conf:
            for line in conf.read().splitlines():
                result.append(line)
            return result
    else:
        return None

settings_dict = load_json_setting('../config/settings.json')
secrets_dict = load_json_setting('../config/secrets.json')
model_dict = load_json_setting('../config/model.json')

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
