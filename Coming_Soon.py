#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 09:38:37 2023

@author: dale
"""

import time
import streamlit as st
from pathlib import Path
import sys

HELPERS_PATH = Path(Path(__file__).parent, '__helpers__')
DATA_PATH = Path(HELPERS_PATH, '.data')

sys.path.append(str(HELPERS_PATH))

import get_gif_to_display as getgif
from __get_image_to_display__ import _img_to_bytes

TEXT_COLOR = 'rgb(206, 194, 235)'
GIVEAWAY_URL = 'http://cannabiscult.co/feb-6th-giveaway'
MO_CANNA_IG = 'https://www.instagram.com/missouricannabisreviews'


def main():
    global TEXT_COLOR, GIVEAWAY_URL, MO_CANNA_IG

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
    top_col = st.container()
    top_col.empty()
#    giveaway_text = f"""
#    <div style="text-align: center;">
#    <a href="{GIVEAWAY_URL}">
#    <h2 style="color:{TEXT_COLOR};">
#    Click here to enter our Party Pack Giveaway
#    </h2>
#    </div>
#    """
#    st.markdown(giveaway_text, unsafe_allow_html=True)
    st.markdown('<div><br></div>', unsafe_allow_html=True)
    visit_sponsers_text = f"""
    <div style="text-align: center;">
    <h2 style="color:{TEXT_COLOR};">
    Visit our sponsors by clicking on their logo to get prepared for the 6th
    </h2>
    </div>
    """
    st.markdown(visit_sponsers_text, unsafe_allow_html=True)
    st.markdown('<div><br></div>', unsafe_allow_html=True)
    # Vivid company logo
    vivid_url = 'https://vividcannabis.com/'
    vivid_img = Path(DATA_PATH, 'png', 'vivid_logo.png')
    vivid_html = _get_temp_sponsor_image_html(vivid_url, vivid_img)
    # Vivid logo above
    # Ruby Glass logo below
    ruby_url = 'https://rubyglassco.com/'
    ruby_img = Path(DATA_PATH, 'png', 'ruby_glass_circle.png')
    ruby_html = _get_temp_sponsor_image_html(ruby_url, ruby_img)
    # Ruby Glass logo above
    # Cannabis Cult Logo below
    cc_img = Path(DATA_PATH, 'png', 'white_cc_logo.png')
    cc_html = _get_temp_sponsor_image_html(MO_CANNA_IG, cc_img)
    # Cannabis Cult Logo above
    with st.container():
        col1, col2, col3 = st.columns([4, 4, 4])
        col1.markdown(vivid_html, unsafe_allow_html=True)
        col2.markdown(ruby_html, unsafe_allow_html=True)
        col3.markdown(cc_html, unsafe_allow_html=True)
    st.markdown('<div><br><br></div>', unsafe_allow_html=True)
    message_text = f"""
    <div style="text-align: center;">
    <a href="{MO_CANNA_IG}">
    <h2 style="color: {TEXT_COLOR};">
    Send The Cannabis Cult a message on Instagram Today
    </h2>
    <br>
    </div>
    """
    st.markdown(message_text, unsafe_allow_html=True)
    # adding gif to top of page last to help load time
    time.sleep(.5)
    with top_col:
        gif_path = Path(DATA_PATH, 'gif', 'cc_coming_soon_large.gif')
        cc_gif = getgif._return_gif_html_with_ref(gif_path, GIVEAWAY_URL)
        st.markdown(cc_gif, unsafe_allow_html=True)


def _get_temp_sponsor_image_html(web_path: str,
                                 img_path: str):
    _url = web_path.replace("https://", "")
    temp_url = _url.replace("www.instagram", "")
    clean_url = temp_url.replace(".com/", "")
    try:
        img_html = f"""
        <div style="text-align: center;">
        <a href='{web_path}'>
        <img src='data:image/png;base64,{_img_to_bytes(img_path)}'>
        <h4><u>{clean_url}</u></h4>
        </a>
        </div>
        """
    except:
        img_html = f"""
        <div style="text-align:center;">
        <a href='{web_path}'>
        <img src='data:image/jpg;base64,{_img_to_bytes(img_path)}'>
        <h4><u>{clean_url}</u></h4>
        </a>
        </div>
        """
    return img_html


if __name__ == '__main__':
    st.set_page_config(
        layout='wide',
        page_title='Cannabis Cult - Coming Soon',
        menu_items=None,
        initial_sidebar_state='collapsed',
    )
    from are_you_21 import mj_app_age_check, _cache_age_result
    age_result = mj_app_age_check()
    cached_result = _cache_age_result(age_result)
    if cached_result:
        main()
