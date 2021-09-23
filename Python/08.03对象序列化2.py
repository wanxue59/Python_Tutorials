# -*- coding: utf-8 -*-
"""
Project: Tutorials
File Name: 08.03对象序列化2
Author: wjz
date: 2021-09-09
"""

import json

def load_pubconf(config_path):
    with open(config_path, 'r') as f:
        configs = json.load(f)
        print(configs)

load_pubconf("D:\PyCharm_Code\Work\APA\PUBLIC\mq\mq_config.json")