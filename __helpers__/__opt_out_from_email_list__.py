#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 10:27:29 2023

@author: dale
"""

import pandas as pd
from pathlib import Path

ENTRIES_GS = '1M1npq3ziMhY5e-0RxzG6Z4dhk1zPkQqAE5RW5okdehA', '828187799'
DOCS_URL = f'https://docs.google.com/spreadsheets/d/{ENTRIES_GS[0]}/export?format=csv&gid={ENTRIES_GS[1]}'


def _get_local_entries_workbook(entries_wbook_path: str):
    entries_wbook_path = Path(entries_wbook_path)
    if entries_wbook_path.is_file():
        return pd.read_csv(str(entries_wbook_path))
    else: 
        return pd.DataFrame(columns=['email'])


def _remove_email_from_entries(email_str: str, 
                               ) -> pd.DataFrame:
    entries_dir = Path(Path(__file__).parent, 'entries')
    entries_wbook_path = Path(entries_dir, 'giveaway_entries_workbook.csv')
    data = _get_local_entries_workbook(entries_wbook_path)
    if (email_str.lower()) in [_email.lower() for _email in data['email'].values]:
        removed_data = data.loc[~
            (data['email'].str.lower()).str.contains(email_str.lower())
            ]
        removed_data.to_csv(str(entries_wbook_path), index=False)
      
