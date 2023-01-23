#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 11:15:50 2023
@author: brettkoenig
"""

import requests
import json
import streamlit.components.v1 as components


proj_url = "https://grapedrop.com/api/v1/projects"
api = "E57tCLsxwzgB4jaTlNabqYe4GtmnQI40yQaxbvGfxwIRQUUn3h5X7KGKWOytJbti"

def data_grab():
    def api_check():
        def get_data(proj_url, api):
            response = requests.get(f"{proj_url}", headers = {"X-API-Key":api})
            if response.status_code == 200:
                jdata = response.json()
                return jdata
                print(jdata)
                print("Success")

            else:
                print(f"error {response.status_code}")

        data = get_data(proj_url, api)
        data_dict = data[0]

        return data_dict

    lp_dict = api_check()
    lp_url = lp_dict.get('url')

    return lp_url


def main():
    url = data_grab()
    url_fix = str("https://" + url)
    components.iframe(url_fix, width=1920, height= 1080)

if __name__ == '__main__':
    main()
