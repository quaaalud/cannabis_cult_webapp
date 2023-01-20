# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import regex as re
import time


def _check_name_is_ascii(name: str) -> str:
    if name.isascii():
        return name.capitalize()
    else:
        return ''
    
def _check_string_is_digits(digit_str: str) -> str:
    if digit_str.isdigit():
        return digit_str
    else:
        return ''
    
def _confirm_email_is_valid(email_str: str) -> str:
    email_regex = re.compile(
        r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])"
    )
    if re.fullmatch(email_regex, email_str):
        return email_str
    else:
        return ''
    

def _check_phone_numbers(phone: str) -> str:
    remchars = ['(', ')', '-', '+', ' ']
    for char in phone:
        if char in remchars:
            phone = phone.replace(char, '')
    if phone.isnumeric():
        return phone
    else:
        return ''
    
    
def get_contact_info(name: str,
                     email: str,
                     phone='',
                     zip_code='') -> dict:
    valid_email = _confirm_email_is_valid(email)
    if valid_email:
        return {
            'name': _check_name_is_ascii(name),
            'email': email,
            'phone': _check_phone_numbers(phone),
            'zip': _check_string_is_digits(zip_code),
        }
    else:
        return None
    
    
def _subscribe_disclaimer() -> str:
    return """
    <h4 style="text-align:left;">
    By subscribing, you agree to the Cannabis Cult User Agreement and 
    Privacy Statement, and that you are at least 21 years old.
    <br>
    </h4>
    """


def _giveaway_form():
    main_block = st.empty()
    with main_block:
        with st.form('giveaway_form'):
            entry_name = st.text_input(
                'Name',
                max_chars=30,
                placeholder='Your Name',
                label_visibility='collapsed',
            )
            email_add = st.text_input(
                'Email',
                max_chars=30,
                placeholder='Email is Required',
                label_visibility='collapsed',
            )
            phone_num = st.text_input(
                'Phone', 
                max_chars=14,
                placeholder='Phone Number',
                label_visibility='collapsed',
            )
            zip_code = st.text_input(
                'Zip Code', 
                max_chars=7,
                placeholder='Zip Code',
                label_visibility='collapsed',
            )
            checkbox_val = st.checkbox(label='21 +', label_visibility='hidden')
            st.markdown(_subscribe_disclaimer(), unsafe_allow_html=True)
            st.markdown('<br>', unsafe_allow_html=True)
            submitted = st.form_submit_button("Submit")
        if submitted:
            main_block.empty()
            if checkbox_val and _confirm_email_is_valid(email_add):
                contact_info = get_contact_info(
                    entry_name,
                    email_add,
                    phone_num,
                    zip_code,
                    )
                main_block.write(contact_info)
                time.sleep(3)
            else:
                main_block.write('You must be 21 years old and a legal resident of Missouri or Illinois')
            
            
    
    