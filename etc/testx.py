#!/usr/bin/env python3
# coding=utf-8
# author: @netwookie.
# -*- coding: utf-8 -*-
"""
This is a test file that tests the API
"""
import urllib3
urllib3.disable_warnings()
from pypheus.network import Network
from pypheus.storage import Storage
from pypheus.logs import Logs
from pypheus.monitoring import Monitoring
import json
import requests

host='10.132.0.153'
username='xod442'
password='ilike2Rock@'



logs = Logs(host,username,password)
info = logs.get_all_logs()
for l in info['data']:
    print('==================Log File===============')
    print(l)
