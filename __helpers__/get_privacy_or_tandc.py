#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 11:51:16 2023

@author: dale
"""

import streamlit as st
from pathlib import Path

HELPERS_DIR = Path(__file__).parents[0]

@st.cache
def _get_html_file(file_name: str) -> str:
    global HELPERS_DIR
    html_doc = Path(HELPERS_DIR, file_name)
    with open(html_doc, 'r') as file:
        return ''.join(file.readlines())
    
    
def _streamlit_display_html(html_str: str) -> st.markdown:
    return st.markdown(html_str, unsafe_allow_html=True)


def _display_privacy_policy():
    _streamlit_display_html(_get_html_file('privacy_policy.html')) 
    

def _display_tandc_policy():
    _streamlit_display_html(_get_html_file('terms_and_conditions.html')) 
    

def return_main_link():
    terms_link = """
    <div>
        <a href="cannabiscult.co">
            <p style="text-align=right";>
            <u>Go back to The Cannabis Cult</u>
            </p>
        </a>
    <div>
    """
    _streamlit_display_html(terms_link)
    
    
    
def _return_terms_of_use_link():
    terms_link = """
    <div>
        <a href="Terms_of_Use">
            <p style="text-align=right";>
            Views Terms of Use
            </p>
        </a>
    <div>
    """
    _streamlit_display_html(terms_link)
    
    
def _return_privacy_link():
    privacy_link = """
    <div>
        <a href="Privacy_Policy">
            <p>
            Views Privacy Policy
            </p>
        </a>
    <div>
    """
    _streamlit_display_html(privacy_link)
    
    
if __name__ == '__main__':
    pass
