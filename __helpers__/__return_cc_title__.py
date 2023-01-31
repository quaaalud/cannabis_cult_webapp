# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 11:16:09 2023

@author: dludwinski
"""

from pathlib import Path
import streamlit as st


def _return_cc_title() -> str:
    from __get_image_to_display__ import return_image_from_path
    cc_logos_path = Path(Path(__file__).parent, '.data', 'cc_logos')
    use_logo = Path(cc_logos_path, 'black_cc_logo.png')
    return st.image(return_image_from_path(str(use_logo)))
