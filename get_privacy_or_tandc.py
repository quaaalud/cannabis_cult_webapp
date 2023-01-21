#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 11:51:16 2023

@author: dale
"""

import streamlit as st
from pathlib import Path

HELPERS_DIR = Path(Path(__file__).parent, '__helpers__')

def _get_privacy_policy_html() -> str:
    global HELPERS_DIR
    privacy_doc = Path(HELPERS_DIR, 'privacy_policy.html')
    with open(privacy_doc, 'r') as file:
        return ''.join(file.readlines())
    

def _get_t_and_c_html() -> str:
    global HELPERS_DIR
    privacy_doc = Path(HELPERS_DIR, 'terms_and_conditions.html')
    with open(privacy_doc, 'r') as file:
        return ''.join(file.readlines())


def _streamlit_display_html_doc(html_str: str) -> st.markdown:
    return st.markdown(html_str, unsafe_allow_html=True)
    
if __name__ == '__main__':
    _streamlit_display_html_doc(_get_privacy_policy_html())
