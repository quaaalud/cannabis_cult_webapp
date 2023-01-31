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
        }


def _get_deal_workbook_and_return_dict() -> dict:
    deals_df = get_gsheet.pandas_read_google_sheet()
    co_names_list = _get_all_company_names(deals_df)
    deals_dict = {}
    for co in co_names_list:
        co_df = deals_df.loc[deals_df.index.str.contains(co)]
        co_vals = _get_all_col_values(co_df)
        deals_dict[co] = _get_company_info_dict(co_vals)
    return deals_dict


def display_daily_deals() -> None:
    deals_dict = _get_deal_workbook_and_return_dict()
    col1, col2, col3 = st.columns([3, 3, 3])
    for i, (co_name, co_info) in enumerate(deals_dict.items()):
        lbl_list = []
        for lbl, info in co_info.items():
            lbl_str = f'{lbl}: {info}'
            lbl_list.append(lbl_str)
        if (i % 3) == 0:
            col2.markdown(
                f"""
                <h2 style="text-align: center">
                {co_name}
                </h2>""",
                unsafe_allow_html=True,
                )
            for lbl in lbl_list:
                col2.markdown(
                    f"""
                    <div style="text-align: center">
                    <h4>
                    {lbl}
                    </h4>
                    </div>
                    """,
                    unsafe_allow_html=True,
                    )
        elif (i % 3) == 1:
            col1.markdown(
                f"""
                <h2 style="text-align: center">
                {co_name}
                </h2>""",
                unsafe_allow_html=True,
                )
            for lbl in lbl_list:
                col1.markdown(
                    f"""
                    <div style="text-align: center">
                    <h4>
                    {lbl}
                    </h4>
                    </div>
                    """,
                    unsafe_allow_html=True,
                    )
        elif (i % 3) == 2:
            col3.markdown(
                f"""
                <h2 style="text-align: center">
                {co_name}
                </h2>""",
                unsafe_allow_html=True,
                )
            for lbl in lbl_list:
                col3.markdown(
                    f"""
                    <div style="text-align: center">
                    <h4>
                    {lbl}
                    </h4>
                    </div>
                    """,
                    unsafe_allow_html=True,
                    )


if __name__ == '__main__':
    display_daily_deals()
