# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 20:52:13 2023

@author: dludwinski
"""

import streamlit as st
import giveaway_form_capture as gform


@st.experimental_singleton(experimental_allow_widgets=True)
def _contest_giveaway_form(wbook_name='giveaway_contest_2'):
    main_block = st.empty()
    with main_block:
        with st.form('contest_form'):
            entry_name = st.text_input(
                'Name',
                max_chars=30,
                placeholder='Your Name',
                label_visibility='collapsed',
                key='GIVEAWAY-NAME',
            )
            email_add = st.text_input(
                'Email',
                max_chars=30,
                placeholder='Email is Required',
                label_visibility='collapsed',
                key='GIVEAWAY-EMAIL',
            )
            phone_num = st.text_input(
                'Phone',
                max_chars=14,
                placeholder='Phone Number',
                label_visibility='collapsed',
                key='GIVEAWAY-PHONE',
            )
            zip_code = st.text_input(
                'Zip Code',
                max_chars=7,
                placeholder='Zip Code',
                label_visibility='collapsed',
                key='GIVEAWAY-ZIP',
            )
            checkbox_val = st.checkbox(
                label='I am at least 21 years old',
                key='GIVEAWAY-CHECKBOX',
                )
            st.markdown(gform._subscribe_disclaimer(), unsafe_allow_html=True)
            st.markdown('<br>', unsafe_allow_html=True)
            submitted = st.form_submit_button(
                "Submit",
                )
        if submitted:
            main_block.empty()
            if checkbox_val and gform._confirm_email_is_valid(email_add):
                contact_info = gform.get_contact_info(
                    entry_name,
                    email_add,
                    phone_num,
                    zip_code,
                )
                data = gform._convert_dict_to_df(contact_info)
                main_block.markdown(
                    """
                <h3 style="text-align:center">
                Your submission has been recorded.<br><br>
                Check your email regularly to see what The Cult is doing<br>
                <br>Updates for Cult Members coming soon!
                </h3>
                """,
                    unsafe_allow_html=True,
                )
                gform._add_new_entry_to_wbook(data, wbook_name=wbook_name)
            else:
                main_block.subheader(
                    """
                    <h3 style="text-align: center;">
                    You must be at least 21 years old &<br>
                    to subscribe to our mailing list.
                    """
                )
