#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, './controllers')
sys.path.append('./domain')
sys.path.append('./repositories')
sys.path.append('.')

from mongo import Mongo
Mongo().db = "mongodb://localhost" 

import bottle, base_controller
bottle.debug(True)
bottle.run(host='0.0.0.0', port=sys.argv[1])

import seeded_data
seeded_data.seed_all_data