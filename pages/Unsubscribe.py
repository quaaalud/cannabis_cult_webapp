#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 18:44:00 2023

@author: dale
"""

import sys
from pathlib import Path

HELPERS_DIR = Path(Path(__file__).parent, '__helpers__')
sys.path.append(str(HELPERS_DIR))

import streamlit as st
from __opt_out_from_email_list__ import _remove_email_from_entries
import get_privacy_or_tandc

def _return_copywrite_text():
    return """
    <section>
    <div>
    © 2023 The Social Outfit. All rights reserved
    </div>
    </section>
    """

def main():
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                div.block-container {padding-top:3rem; padding-bottom:0rem;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    opt_out_text = """
    <div>
    <h2 style="text-align: center">
    You are unsubscribing from<br>The Cannabis Cult<br><br>
    </h2>
    <h6 style="text-align: center">
    To proceed, enter your email address and click "Opt Out"<br><br>
    </h6>
    </div>
    """
    st.markdown(opt_out_text, unsafe_allow_html=True)
    user_email = st.text_input('Email to opt out:')
    opt_out_button = st.button('Opt Out', type='secondary')
    if opt_out_button and (user_email != None):
        _remove_email_from_entries(user_email) 
    sorry_youre_leaving = """
    <div>
    <h4 style="text-align: center">
    We are sad to see you go.<br><br>
    Send us a message at <a href="mailto: contacts@thesocialoutfitus.com"> 
    contacts@thesocialoutfitus.com</a> to let us know how to get you back
    </h4>
    </div>
    """
    st.markdown(sorry_youre_leaving, unsafe_allow_html=True)
    st.markdown('<br><br><br><br><br><br><br><br><br><br><br><br>',
                unsafe_allow_html=True)
    bottom_col, pcol, tcol= st.columns([3, 1.5, 1.5])
    with bottom_col:
        st.markdown(
            f"""
            <label style="text-align:center;">
            {_return_copywrite_text()}
            """,
            unsafe_allow_html=True,
        )
    with pcol:
        get_privacy_or_tandc._return_privacy_link()
    with tcol:
        get_privacy_or_tandc._return_terms_of_use_link()  
        
        
if __name__ == '__main__':
    st.set_page_config(
        page_title='Cannabis Cult - Unsubscrive',
        menu_items=None,
    )
    main()
    
        