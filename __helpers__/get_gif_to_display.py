#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 09:50:38 2023

@author: dale
"""

import base64
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent))


def _return_gif_html(file_path: str) -> str:
    file_ = open(str(file_path), "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return f'''
    <style>
    body {{
        text-align: center;
    }}
    img {{
        max-width: 100%;
        object-fit: cover;
      }}
      .container {{
        height: 100%;
      }}
    </style>
    <div class="container">
    <figure>
    <img src="data:image/gif;base64,{data_url}">
    </figure>
    </div>
    '''


def _return_gif_html_with_ref(file_path: str, url_str: str) -> str:
    file_ = open(str(file_path), "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return f'''
    <style>
    body {{
        text-align: center;
    }}
    img {{
        max-width: 100%;
        object-fit: cover;
      }}
      .container {{
        height: 100%;
      }}
    </style>
    <div class="container">
    <a href="{url_str}";>
    <figure>
    <img src="data:image/gif;base64,{data_url}">
    </figure>
    </a>
    </div>
    '''

if __name__ == '__main__':
    pass
