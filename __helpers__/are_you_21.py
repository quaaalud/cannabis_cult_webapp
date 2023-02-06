# -*- coding: utf-8 -*-
"""
Streamlit container to determine if the user is 21 + years old
Created on Sun Jan  1 19:42:09 2023

@author: dludwinski
"""

import time
import streamlit as st
import datetime as dt


def _get_21_disclaimer_text() -> str:
    return """Potential customers should be reminded that the possession, distribution,
    and cultivation of cannabis is still prohibited under US federal law.
    Medical decisions should not be based on advertising.
    Consult a physician of the benefits and risks of of particular medical
    marijuana products.
    """


def get_date_str_21_years_ago() -> str:
    """
    Get date from 21 years prior to the current date.

    Returns
    -------
    str
        Date formatted "Month Day, Year"

    """
    t_date = dt.date.today()
    min_year = t_date.year - 21
    mnth_day = t_date.strftime('%b %d')
    return f'{mnth_day}, {min_year}'


@st.experimental_singleton(suppress_st_warning=True,
                           experimental_allow_widgets=True)
def are_you_21() -> bool:
    """
    Determine if user is 21 and return bool.

    Retruns True if user selects Yes and False if user selects No
    """
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                div.block-container
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    display_txt = f'Were you born on or before {get_date_str_21_years_ago()}?'
    col1, col2, col3 = st.columns([1.5, 9, 1.5])
    col2.markdown(
        f"""
        <section>
        <h2 style="color:#301934; text-align:center">
        {display_txt}
        </h2>
        </section>""", 
        unsafe_allow_html=True
        )
    e1, col1, col2, e2 = st.columns([5.5, 1, 1, 5.5])
    yes_button = col1.button('Yes', key='YES-KEY')
    no_button = col2.button('No', key='NO-KEY')
    e1, disclaim_col, e2 = st.columns([2.5, 7, 2.5])
    disclaim_col.markdown(
        f"""<section>
        <h4 style="text-align:center">
        <small><small>
        {_get_21_disclaimer_text()}""", 
        unsafe_allow_html=True
        )
    if no_button:
        return False
    if yes_button:
        return True


@st.experimental_singleton(suppress_st_warning=True,
                           experimental_allow_widgets=True)
def mj_app_age_check() -> bool:
    """
    Confirm the user is over 21 and if so, proceeds to call display functions.

    Returns
    -------
    None.

    """
    head_block = st.container()
    main_block = st.container()
    with main_block:
        age_result = are_you_21()
    if age_result is False:
        main_block.empty()
        head_block.subheader('Come back with someone over the age of 21')
        time.sleep(30)
        head_block.empty()
        return False
    elif age_result is True:
        main_block.empty()
        head_block.subheader('Welcome to the Cannabis Cult!')
        time.sleep(2.5)
        head_block.write('')
        return True


@st.cache
def _cache_age_result(any_var):
    return any_var


if __name__ == '__main__':
    pass
