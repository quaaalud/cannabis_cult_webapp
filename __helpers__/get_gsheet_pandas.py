# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 15:40:23 2023

@author: dludwinski
"""

import pandas as pd

SPREADSHEET_ID = '1XiihVY96k3u2eOQvNO2LxYSgBbqm3BA3MeTt7PH2qB4'


def pandas_read_google_sheet(wbook_id=SPREADSHEET_ID) -> pd.DataFrame:
    """
    Return Pandas DataFrame with Daily Deals Google Sheets.

    Parameters
    ----------
    wbook_id : str
        String from url identifying google sheets workbook

    Returns
    -------
    pd.DataFrame(columns=['name', 'phone', 'Daily Deal', 'Promo Code'])

    """
    return pd.read_csv(
        f'https://docs.google.com/spreadsheets/d/{wbook_id}/export?format=csv&gid=0',
    ).dropna(axis=1).set_index('name')


if __name__ == '__main__':
    data = pandas_read_google_sheet()
    print(data)
