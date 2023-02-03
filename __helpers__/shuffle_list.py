# -*- coding: utf-8 -*-

from random import shuffle
import streamlit as st


def _check_for_list_cache_and_shuffle(any_list: list) -> list:
    if 'list_shuffle' not in st.session_state.keys():
        shuffle(any_list)
        st.session_state['list_shuffle'] = True
        return any_list
    else:
        return any_list
