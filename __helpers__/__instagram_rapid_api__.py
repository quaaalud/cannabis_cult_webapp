#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 22:57:49 2023

@author: dale
"""

import os
import requests
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


url = "https://instagram47.p.rapidapi.com/stories"

querystring = {"user_id": "55792533995", "batch_size": "20"}

headers = {
	"X-RapidAPI-Key": os.getenv('INSTAGRAM_API_KEY'),
	"X-RapidAPI-Host": os.getenv('INSTAGRAM_HOST')
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(dir(response))
print(response.reason)
print(response)
