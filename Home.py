# -*- coding: utf-8 -*-
"""Local Cannibus Dispensary Deals Website made with Streamlit

Created on Sun Jan  1 18:31:44 2023

@author: dludwinski
"""

import streamlit as st
import sys
from pathlib import Path

MAIN_DIR = Path(__file__).parent
sys.path.append(str(MAIN_DIR))
sys.path.append(str(Path(MAIN_DIR, '__helpers__')))

import are_you_21
from __return_cc_title__ import _return_cc_title
import __get_reviews_insta__
import daily_deals

FONT_FAMILY = 'font-family:"Helvetica Neue", Arial, Helvetica, Verdana,'

def mj_app_display() -> None:
    """Display the Cannabis Cult Web App."""
    # Hide mainmenu and footer
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                ul {display: none;}
                div.block-container {padding-top:1rem; padding-bottom:0rem;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.markdown('<div><br></div>', unsafe_allow_html=True)
    st.markdown(_return_cc_title(), unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2, 2, 2])
    col1.write('Image Placeholder')
    col2.markdown(
        __get_reviews_insta__._get_insta_html(),
        unsafe_allow_html=True
    )
    col3.write('Image Placeholder')
    st.markdown('<div><br><br></div>', unsafe_allow_html=True)
    daily_deals.display_daily_deals()
    st.markdown('<div><br></div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div style="text-align: center;">
        <h1>Map Placeholder</h1>
        </div>""",
        unsafe_allow_html=True,
    )
    st.markdown('<div><br></div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div style="text-align: center;">
        <h1>Bottom of page placeholder</h1>
        </div>""",
        unsafe_allow_html=True,
    )
    st.markdown('<div><br></div>', unsafe_allow_html=True)


if __name__ == '__main__':
    st.set_page_config(
        layout='wide',
        page_title='Cannabis Cvlt',
        menu_items=None,
        initial_sidebar_state='collapsed',
    )
    if are_you_21.mj_app_age_check():
        mj_app_display()
