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
    from __return_cc_title__ import _return_cc_title
    import asyncio
    import daily_deals
    import __image_carousel__
    import giveaway_form_capture
    import __add_pages_links__
    import __sm_links__
    import get_video_to_display
    import __add_shopify_link__
    from __add_background_from_local__ import add_bg_from_local
    import shuffle_list
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
    GIVEAWAY_BG_PATH = Path(
        Path(__file__).parent, '__helpers__', '.data', 'jpg', 'giveaway_bg.jpg'
        )
    add_bg_from_local(GIVEAWAY_BG_PATH)
    st.markdown('<div><br></div>', unsafe_allow_html=True)
    # import and shuffle list on the first run only
    png_list = __image_carousel__._return_img_carousel_files()
    all_png_list = shuffle_list._check_for_list_cache_and_shuffle(png_list)
    e1, logo_col, e2 = st.columns([4, 3, 4])
    with logo_col:
        _return_cc_title()
    st.markdown('<div><br></div>', unsafe_allow_html=True)
    e1, vid_col, e2 = st.columns([1.5, 7, 1.5])
    carousel_container = st.container()
    st.markdown('<div><br></div>', unsafe_allow_html=True)
    daily_deals.display_daily_deals()
    st.markdown('<div><br><br></div>', unsafe_allow_html=True)
    with st.expander('Join our mailing list', expanded=True):
        giveaway_form_capture._giveaway_form()
        st.markdown(_get_disclaimer_text(), unsafe_allow_html=True)
    st.markdown('<div><br></div>', unsafe_allow_html=True)
    __sm_links__._display_sm_links()
    __add_pages_links__._display_pages_links()
#    vid_bytes, vid_type = get_video_to_display._display_current_video()
    with vid_col:
        __add_shopify_link__._add_shopify_merch_link()
    with carousel_container:
        asyncio.run(
            __image_carousel__._return_image_carousel(
                all_png_list,
                set_height=250
            )
        )


if __name__ == '__main__':
    icon_path = Path(
        Path(__file__).parent, '__helpers__', '.data', 'png', 'cannabis_cult_logo.png'
        )
    import __get_image_to_display__ as get_image
    st.set_page_config(
        layout='wide',
        page_title='The Cannabis Cult',
        page_icon=get_image.return_image_from_path(icon_path),
        menu_items=None,
        initial_sidebar_state='collapsed',
    )
    import are_you_21
    if 'age_check' not in st.session_state.keys():
        st.session_state['age_check'] = False
    if st.session_state['age_check'] is False:
        st.session_state['age_check'] = are_you_21.mj_app_age_check()
    else:
        mj_app_display()
