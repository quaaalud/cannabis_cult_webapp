# -*- coding: utf-8 -*-

from random import shuffle
import streamlit as st


@st.cache()
def _check_for_list_cache_and_shuffle(any_list: list) -> list:
    if st.session_state.get('list_shuffle') is True:
        return any_list.copy()
    elif 'list_shuffle' not in st.session_state.keys():
        shuffle(any_list)
        st.session_state['list_shuffle'] = True
        return any_list
    else:
        pass
