# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import regex as re
from datetime import date
from pandas import Timestamp
from pathlib import Path
import sys

HELPERS_DIR = Path(__file__).parent
sys.path.append(str(HELPERS_DIR))
ENTRIES_GS = '1M1npq3ziMhY5e-0RxzG6Z4dhk1zPkQqAE5RW5okdehA', '828187799'
DOCS_URL = f'https://docs.google.com/spreadsheets/d/{ENTRIES_GS[0]}/export?format=csv&gid={ENTRIES_GS[1]}'
ENTRIES_DIR = Path(HELPERS_DIR, 'entries')


def _check_name_is_ascii(name: str) -> str:
    if name.isascii():
        return name.title()
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
        today = Timestamp(date.today())
        return {
            'name': _check_name_is_ascii(name),
            'email': email,
            'phone': _check_phone_numbers(phone),
            'zip': _check_string_is_digits(zip_code),
            'date': str(today),
        }
    else:
        return None


def _convert_dict_to_df(data_dict: dict) -> pd.DataFrame:
    if isinstance(data_dict, dict):
        return pd.DataFrame.from_dict(data_dict, orient='index').transpose()


def _get_entries_workbook():
    global DOCS_URL
    entry_wbook = pd.read_csv(DOCS_URL)
    return entry_wbook


def _get_local_workbook():
    global ENTRIES_DIR
    ENTRIES_DIR.mkdir(exist_ok=True)
    try:
        return pd.read_csv(
            str(Path(ENTRIES_DIR, 'giveaway_entries_workbook.csv'))
            )
    except FileNotFoundError:
        col_list = ['name', 'email', 'phone', 'zip', 'date']
        return pd.DataFrame(columns=col_list)


def _add_new_entry_to_wbook(df: pd.DataFrame) -> pd.DataFrame:
    global DOCS_URL, ENTRIES_DIR
    entry_wbook = _get_entries_workbook()
    emails = entry_wbook['email'].unique()
    local_workbook = _get_local_workbook()
    local_emails = local_workbook['email'].unique()
    temp_df = pd.concat([local_workbook, entry_wbook], axis=0)
    if [df['email'].unique()][0] not in emails and [
            df['email'].unique()][0] not in local_emails:
        new_df = pd.concat(
            [df, temp_df],
            axis=0
            ).drop_duplicates(subset=['email'])
    else:
        new_df = temp_df.copy()
    new_df.to_csv(DOCS_URL, index=False)
    new_df.to_csv(
        str(Path(ENTRIES_DIR, 'giveaway_entries_workbook.csv')),
        index=False
        )
    return len(new_df)


def _subscribe_disclaimer() -> str:
    return """
    <h4 style="text-align:left;">
    By subscribing, you agree to the Cannabis Cult
    <a href="http://cannabiscult.co/Terms_of_Use">User Agreement</a> and
    <a href="http://cannabiscult.co/Privacy_Policy">Privacy Statement</a>,
    and that you are at least 21 years old.
    <br>
    </h4>
    """


@st.experimental_singleton(experimental_allow_widgets=True)
def _giveaway_form():
    main_block = st.empty()
    with main_block:
        with st.form('giveaway_form'):
            entry_name = st.text_input(
                'Name',
                max_chars=30,
                placeholder='Your Name',
                label_visibility='collapsed',
                key='FORM-NAME',
            )
            email_add = st.text_input(
                'Email',
                max_chars=30,
                placeholder='Email is Required',
                label_visibility='collapsed',
                key='FORM-EMAIL',
            )
            phone_num = st.text_input(
                'Phone',
                max_chars=14,
                placeholder='Phone Number',
                label_visibility='collapsed',
                key='FORM-PHONE',
            )
            zip_code = st.text_input(
                'Zip Code',
                max_chars=7,
                placeholder='Zip Code',
                label_visibility='collapsed',
                key='FORM-ZIP',
            )
            checkbox_val = st.checkbox(
                label='I am at least 21 years old',
                key='FORM-CHECKBOX',
                )
            st.markdown(_subscribe_disclaimer(), unsafe_allow_html=True)
            st.markdown('<br>', unsafe_allow_html=True)
            submitted = st.form_submit_button(
                "Submit",
                )
        if submitted:
            main_block.empty()
            if checkbox_val and _confirm_email_is_valid(email_add):
                contact_info = get_contact_info(
                    entry_name,
                    email_add,
                    phone_num,
                    zip_code,
                )
                data = _convert_dict_to_df(contact_info)
                main_block.markdown(
                    """
                <h3 style="text-align:center">
                Your submission has been recorded.<br><br>
                Check your email regularly to see if you have won,<br><br>
                We have lots surprises in store for Cult Members coming soon!
                </h3>
                """,
                    unsafe_allow_html=True,
                )
                _add_new_entry_to_wbook(data)
            else:
                main_block.subheader(
                    """
                    <h3 style="text-align: center;">
                    You must be at least 21 years old &<br>
                    legal resident of Missouri or Illinois to Enter
                    """
                )
