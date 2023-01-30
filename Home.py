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


from __return_cc_title__ import _return_cc_title
import asyncio
import daily_deals
import __image_carousel__
import are_you_21
import giveaway_form_capture
import __add_pages_links__
import __sm_links__


FONT_FAMILY = 'font-family:"Helvetica Neue", Arial, Helvetica, Verdana,'


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


def mj_app_display() -> None:
    """Display the Cannabis Cult Web App."""
    # Hide mainmenu and footer
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                div.block-container
                {padding-top:1rem; padding-bottom:0rem;}
                footer {visibility: hidden;}
                </style>
                """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.markdown('<div><br></div>', unsafe_allow_html=True)
    st.markdown(_return_cc_title(), unsafe_allow_html=True)
    daily_deals.display_daily_deals()
    st.markdown('<div><br></div>', unsafe_allow_html=True)
    carousel_container = st.container()
    st.markdown('<div><br><br></div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div style="text-align: center;">
        <h1>Map or Highlighted Content Placeholder</h1>
        </div>""",
        unsafe_allow_html=True,
    )
    st.markdown('<div><br></div>', unsafe_allow_html=True)
    with st.expander('Join our mailing list'):
        giveaway_form_capture._giveaway_form()
        st.markdown(_get_disclaimer_text(), unsafe_allow_html=True)
    st.markdown('<div><br></div>', unsafe_allow_html=True)
    __sm_links__._display_sm_links()
    __add_pages_links__._display_pages_links()
    with carousel_container:
        asyncio.run(__image_carousel__._return_image_carousel())


if __name__ == '__main__':
    st.set_page_config(
        layout='wide',
        page_title='The Cannabis Cult',
        menu_items=None,
        initial_sidebar_state='collapsed',
    )
    mj_app_display()
