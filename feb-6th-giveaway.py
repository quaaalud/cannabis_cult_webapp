# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 16:18:38 2023

@author: dludwinski
"""

import streamlit as st
import sys
from pathlib import Path

HELPERS_PATH = Path(Path(__file__).parents[0], '__helpers__')
DATA_PATH = Path(HELPERS_PATH, '.data')
sys.path.append(str(HELPERS_PATH))

from __add_background_from_local__ import add_bg_from_local
from local_image_to_html_with_href import _clickable_image_without_caption
from giveaway_form_capture import _giveaway_form
import get_privacy_or_tandc
import __sm_links__


def _get_disclaimer_text() -> str:
    return """
    <p style="text-align:center;">
    <small><small><small>
    Potential customers should be reminded that the possession, distribution,
    and cultivation of cannabis is still prohibited under US federal law.
    Medical decisions should not be based on advertising.
    Consult a physician of the benefits and risks of of particular medical
    marijuana products.
    </small></small></small>
    </p>
    """


def _get_subscribe_to_win_text() -> str:
    return """
    <h1 style="text-align:center;">
    Subscribe to The Cannabis Cult<br>
    Enter for a chance to win the Rec-Day Party Pack!
    </h1>
    """


def _get_sponsors_text() -> str:
    return """
    <h1 style="text-align:left;">
        Featuring art by <span style="color:#c52138;">Ruby Pearl Co.
        </span><br>
        Sponsored by:<br>
          <span style="color:#ec5328">Vivid Cannabis</span><br>
          <span style="color:#0a7840">NatureMed </span><br>
          <span style="color:#ecb21f">Dispensary</span><br>
          <span style="color:#e2c36a">Handwraps Paper Co.</span><br>
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
    # Hide mainmenu and footer
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                ul {display: none;}
                div.block-container {padding-top:1rem; padding-bottom:0rem;}
                footer {visibility: hidden;}
                </style>
                """
    st_allow_markdown(hide_streamlit_style)
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
            st_allow_markdown(_get_disclaimer_text())
            st.markdown('</span></div><br><br><br>', unsafe_allow_html=True)

    # sponsor logo paths
    with st.container():
        VIVID_LOGO = Path(DATA_PATH, 'png', 'vivid_logo.png')
        VIVID_URL = 'https://vividcannabis.com/'
        NATUREMED_LOGO = Path(DATA_PATH, 'png', 'naturemedlogo(stack)2023.png')
        NATUREMED_URL = 'https://naturemedmo.com/ofallon/'
        RUBYGLASS_LOGO = Path(DATA_PATH, 'png', 'ruby_glass_circle.png')
        RUBYGLASS_URL = 'https://rubyglassco.com/'
        HANDWRAPS_LOGO = Path(DATA_PATH, 'png', 'handwraps_logo.png')
        HANDWRAPS_URL = 'https://handwrapsco.com/'
        CC_LOGO = Path(DATA_PATH, 'png', 'white_cc_logo.png')
        CC_INSTA_URL = 'https://www.instagram.com/missouricannabisreviews'
        col1, col2, col3 = st.columns([2, 2, 2,])
        with col1:
            st_allow_markdown(
                _clickable_image_without_caption(VIVID_URL, VIVID_LOGO)
            )
            st.markdown('<br><br><br>', unsafe_allow_html=True)
            st_allow_markdown(
                _clickable_image_without_caption(NATUREMED_URL, NATUREMED_LOGO)
            )
            st.markdown('<br><br><br>', unsafe_allow_html=True)
        with col2:
            st_allow_markdown(
                _clickable_image_without_caption(HANDWRAPS_URL, HANDWRAPS_LOGO)
            )
            st.markdown('<br><br><br>', unsafe_allow_html=True)
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
    # social medial links for The Cannabis Cult
    with st.container():
        __sm_links__._display_sm_links()
    e1, bottom_col, e2, pcol, tcol, e3 = st.columns([.5, 3, .25,  1, 1, .5])
    # bottom of page copywrite
    with bottom_col:
        st_allow_markdown(
            f"""
            <label style="text-align:center;">
            {_return_copywrite_text()}

            """
        )
    with pcol:
        get_privacy_or_tandc._return_privacy_link()
    with tcol:
        get_privacy_or_tandc._return_terms_of_use_link()


if __name__ == '__main__':
    st.set_page_config(
        layout='wide',
        page_title='Cannabis Cult - Feb 6th Giveaway',
        menu_items=None,
        initial_sidebar_state='collapsed',
    )
    giveaway_page()
