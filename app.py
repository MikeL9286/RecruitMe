#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, './controllers')
sys.path.append('./domain')
sys.path.append('./repositories')
sys.path.append('.')

import bottle, base_controller

from sys import argv

bottle.debug(True)
bottle.run(host='0.0.0.0', port=argv[1])