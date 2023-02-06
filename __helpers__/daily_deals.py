# -*- coding: utf-8 -*-
"""
Script to import the Menu options to main script

Created on Mon Jan 2 18:45:22 2023

@author: dludwinski
"""


from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent))

import streamlit as st
import pandas as pd
import get_gsheet_pandas as get_gsheet
from numpy import array


def _get_number_of_deals(df: pd.DataFrame) -> int:
    return len(df)


def _get_all_company_names(df: pd.DataFrame) -> pd.DataFrame:
    return [name for name in df.index.unique()]


def _get_all_col_values(df: pd.DataFrame) -> list:
    return df.values


def _get_company_info_dict(vals_array: array) -> dict:
    return {
        'Contact': vals_array[0][0],
        'Address': vals_array[0][1],
        'Try This': vals_array[0][2],
        'Specials': vals_array[0][3],
        'Image': vals_array[0][4],
        }


def _get_deal_workbook_and_return_dict() -> dict:
    deals_gsheet = get_gsheet.pandas_read_google_sheet()
    deals_df = deals_gsheet.copy().fillna(' ')
    co_names_list = _get_all_company_names(deals_df)
    deals_dict = {}
    for co in co_names_list:
        co_df = deals_df.loc[deals_df.index.str.contains(co)]
        co_vals = _get_all_col_values(co_df)
        deals_dict[co] = _get_company_info_dict(co_vals)
    return deals_dict


def display_daily_deals() -> None:
    deals_dict = _get_deal_workbook_and_return_dict()
    deals_container = st.container()
    with deals_container:
        col1, col2 = st.columns([4, 4])
        for i, (co_name, co_info) in enumerate(deals_dict.items()):
            lbl_list = []
            for lbl, info in co_info.items():
                lbl_str = f'{info}'
                lbl_list.append(lbl_str)
            if (i % 2) == 0:
                col2.markdown(
                    f"""
                    <h1 style="text-align: center; 
                    font-family: taurunum-ferrum-iron, sans-serif;
                    font-style: normal";>
                    {co_name}
                    </h1>""",
                    unsafe_allow_html=True,
                    )
                for lbl in lbl_list:
                    if lbl.startswith('https:'):
                        col2.image(
                            f'{lbl}',
                            use_column_width='always',
                            )
                    else:
                        col2.markdown(
                            f"""
                            <h3 style="text-align: center; 
                            font-family: taurunum-ferrum-iron, sans-serif;
                            font-style: normal";>
                            {lbl}
                            </h3>
                            """,
                            unsafe_allow_html=True,
                            )
                col2.markdown('<br><br>', unsafe_allow_html=True)
            elif (i % 2) == 1:
                col1.markdown(
                    f"""
                    <h1 style="text-align: center; 
                    font-family: taurunum-ferrum-iron, sans-serif;
                    font-style: normal";>
                    {co_name}
                    </h1>""",
                    unsafe_allow_html=True,
                    )
                for lbl in lbl_list:
                    if lbl.startswith('https:'):
                        col1.image(
                            f'{lbl}',
                            use_column_width='always',
                            )
                    else:
                        col1.markdown(
                            f"""
                            <h3 style="text-align: center; 
                            font-family: taurunum-ferrum-iron, sans-serif;
                            font-style: normal";>
                            {lbl}
                            </h3>
                            """,
                            unsafe_allow_html=True,
                            )
                col1.markdown('<br><br>', unsafe_allow_html=True)


if __name__ == '__main__':
    display_daily_deals()
