#!/usr/bin/env python3
__version__ = "0.1.0"

import os
import json

def load_json_setting(path):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    with open(path, 'r') as conf:
        return json.load(conf)

def load_text_list(path):
    result = []
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    with open(path, 'r') as conf:
        for line in conf.read().splitlines():
            result.append(line)
    return result

settings_dict = load_json_setting('../config/settings.json')
secrets_dict = load_json_setting('../config/secrets.json')
amazon_list = load_text_list(settings_dict['amazon_lib'])

outfile = settings_dict['outfile']
max_item_num = settings_dict['max_item_num']

author_black_list = settings_dict['author_black_list']
genle_black_list = settings_dict['genle_black_list']
title_black_list = settings_dict['title_black_list']
min_price = settings_dict['min_price']

amazon_access_key = secrets_dict['amazon_access_key']
amazon_secret_key = secrets_dict['amazon_secret_key']
amazon_assosiate_id = secrets_dict['amazon_assosiate_id']
