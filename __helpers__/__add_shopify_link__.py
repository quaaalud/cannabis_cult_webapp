#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 16:50:38 2023

@author: dale
"""

import streamlit as st
from local_image_to_html_with_href import _clickable_image_without_caption
from pathlib import Path


def _add_shopify_merch_link() -> str:
    shopify_link = 'https://thecannabiscult.myshopify.com/'
    shopify_img = str(
        Path(
            Path(__file__).parent, '.data', 'cc_logos', 'cc_cult_hoodie.png'
        )
    )
    html_str = f"""
    <div>
    <h1 style="text-align: center;">
    <a href="{shopify_link}" style="color: #301934;">
    First edition merchandise now available!
    </a>
    </h1>
    </div>
    """
    shopify_container = st.container()
    with shopify_container:
        st.markdown(
            _clickable_image_without_caption(shopify_link, shopify_img),
            unsafe_allow_html=True,
        )
        st.markdown(html_str, unsafe_allow_html=True)
