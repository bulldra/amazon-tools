#!/usr/bin/env python3
__version__ = "0.1.0"

import os
import json

def load_json_setting(path):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    with open(path, 'r') as conf:
        return json.load(conf)

settings_dict = load_json_setting('../config/settings.json')
secrets_dict = load_json_setting('../config/secrets.json')

outfile = settings_dict['outfile']
amazon_access_key = secrets_dict['amazon_access_key']
amazon_secret_key = secrets_dict['amazon_secret_key']
amazon_assosiate_id = secrets_dict['amazon_assosiate_id']
