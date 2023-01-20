# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 16:18:38 2023

@author: dludwinski
"""

import streamlit as st
import sys
from pathlib import Path

HELPERS_PATH = Path(Path(__file__).parent, '__helpers__')
DATA_PATH = Path(HELPERS_PATH, '.data')
sys.path.append(str(HELPERS_PATH))

from __add_background_from_local__ import add_bg_from_local
from local_image_to_html_with_href import _clickable_image_without_caption
from giveaway_form_capture import _giveaway_form


def _get_subscribe_to_win_text() -> str:
    return """
    <h1 style="text-align:center;">
    Subscribe for a chance to win the Rec-Day Party Pack!
    <h1>
    """
    

def _get_sponsors_text() -> str:
    return """
    <h1 style="text-align:left;">
        Featuring art by <span style="color:#e74c3c;">Ruby Pearl Glass Co.
        </span><br>
        Sponsored by:<br>
          <span style="color:#f39c12">Vivid Cannabis</span><br>
          <span style="color:#e74c3c">NatureMed Dispensary</span><br>
          <span style="color:#f39c12">Handwraps STL</span><br>
          <br>
    </h1>
    """
    

def _subscribe_disclaimer() -> str:
    return """
    <label>
    By subscribing, you agree to the Cannabis Cult User Agreement and 
    Privacy Statement, and that you are at least 21 years old.
    <br>
    </label>
    """
    
    
def _return_copywrite_text():
    return """
    <section>
    <div>
    © 2023 The Cannabis Cult. All rights reserved
    </div>
    </section>
    """
    

def giveaway_page():
    global HELPERS_PATH, DATA_PATH
    
    def st_allow_markdown(html_str: str) -> None:
        """
        HTML string to st.markdown with unsafe_allow_html set to True
        Parameters
        ----------
        html_str : str
            DESCRIPTION.

        Returns
        -------
        None

        """
        st.markdown(html_str, unsafe_allow_html=True)
        
    # add background to page
    GIVEAWAY_BG_PATH = Path(DATA_PATH, 'jpg', 'giveaway_bg.jpg')
    add_bg_from_local(GIVEAWAY_BG_PATH)
    
    # subscribe to win text
    with st.container():
        e1, upper_col, e2 = st.columns([.25, 2, .25])
        with upper_col:
            st_allow_markdown(_get_subscribe_to_win_text())
    # submission form
    with st.container():
        e1, text_col, e2, form_col, e3 = st.columns([.5, 2, .25, 2, .5])
        with text_col:
            st_allow_markdown(_get_sponsors_text())
        with form_col:
            st.markdown(
                '<div><span style="text-align: right;">', 
                unsafe_allow_html=True
                )
            _giveaway_form()
            st.markdown('</span></div><br><br><br>', unsafe_allow_html=True)
        
    
    # sponsor logo paths
    with st.container():
        VIVID_LOGO = Path(DATA_PATH, 'png', 'vivid_logo.png')
        VIVID_URL = 'https://vividcannabis.com/'
        NATUREMED_LOGO = Path(DATA_PATH, 'png', 'naturemedlogo(stack)2023.png')
        NATUREMED_URL = 'https://naturemedmo.com/ofallon/'
        RUBYGLASS_LOGO = Path(DATA_PATH, 'png', 'ruby_glass_circle.png')
        RUBYGLASS_URL = 'https://rubyglassco.com/'
        CC_LOGO = Path(DATA_PATH, 'png', 'white_cc_logo.png')
        CC_INSTA_URL = 'https://www.instagram.com/missouricannabisreviews' 
        col1, col2, col3 = st.columns([2, 2, 2,])
        with col1:
            st_allow_markdown(
                _clickable_image_without_caption(VIVID_URL, VIVID_LOGO)
                )
            st.markdown('<br><br><br>', unsafe_allow_html=True)
            st_allow_markdown(
                _clickable_image_without_caption(NATUREMED_URL ,NATUREMED_LOGO)
                )
            st.markdown('<br><br><br>', unsafe_allow_html=True)
        with col2:
            st_allow_markdown(
                _clickable_image_without_caption(CC_INSTA_URL, CC_LOGO)
                )
            st.markdown('<br><br><br>', unsafe_allow_html=True)
        with col3:
            st_allow_markdown(
                _clickable_image_without_caption(RUBYGLASS_URL, RUBYGLASS_LOGO)
                )
            st.markdown('<br><br><br>', unsafe_allow_html=True)
            
    st.markdown('<br><br><br><br><br><br>', unsafe_allow_html=True)
    # bottom of page copywrite
    e1, bottom_col, e2 = st.columns([.5, 1, .5])
    with bottom_col:
        st_allow_markdown(f'<footer style="text-align:center;">{_return_copywrite_text()}</footer>')
    
    

    
                

if __name__ == '__main__':
    st.set_page_config(
        layout='wide',
        page_title='Cannabis Cult - Feb 6th Giveaway',
        menu_items=None,
        initial_sidebar_state='collapsed',
    )
    giveaway_page()
