# -*- coding: utf-8 -*-
"""
Streamlit container to determine if the user is 21 + years old
Created on Sun Jan  1 19:42:09 2023

@author: dludwinski
"""

import time
import streamlit as st
import datetime as dt


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


def are_you_21() -> bool:
    """
    Determine if user is 21 and return bool.

    Retruns True if user selects Yes and False if user selects No
    """
    display_txt = f'Were you born on or before {get_date_str_21_years_ago()}?'
    with st.container():
        col1, col2, col3 = st.columns([3, 2.5, 3])
        col2.write(display_txt)
        e1, col1, col2, e2 = st.columns([5, 1, 1, 5])
        yes_button = col1.button('Yes')
        no_button = col2.button('No')
        if no_button:
            return 'Not 21'
        if yes_button:
            return True


def mj_app_age_check() -> bool:
    """
    Confirm the user is over 21 and if so, proceeds to call display functions.

    Returns
    -------
    None.

    """
    head_block = st.empty()
    main_block = st.empty()
    with main_block:
        age_result = are_you_21()
    if age_result is None:
        pass
    elif age_result == 'Not 21':
        main_block.empty()
        head_block.subheader('Come back with someone over the age of 21')
        time.sleep(30)
        head_block.empty()
        return False
    else:
        main_block.empty()
        head_block.subheader('Welcome to the Cannabis Cult!')
        time.sleep(2.5)
        head_block.write('')
        return True


@st.cache
def _cache_age_result(any_var):
    return any_var
    

if __name__ == '__main__':
    result = are_you_21()
    print(result)
