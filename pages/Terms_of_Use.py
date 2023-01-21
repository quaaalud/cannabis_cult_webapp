#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 13:29:35 2023

@author: dale
"""

import sys
import streamlit as st
from pathlib import Path

HELPERS_PATH = Path(Path(__file__).parents[1], '__helpers__')
sys.path.append(str(HELPERS_PATH))


def main():
    from get_privacy_or_tandc import _display_tandc_policy
    # Hide mainmenu and footer
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                div.block-container {padding-bottom:0rem;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    _display_tandc_policy()


if __name__ == '__main__':
    main()
