#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 21:58:50 2023

@author: dale
"""

from google.colab import drive
from pathlib import Path
import pandas as pd

def _csv_to_google_drive(df: pd.DataFrame,
                         google_path: str,
                         save_name: str) -> pd.DataFrame:
    try:
        drive.mount(google_path)
        save_path = Path(google_path, save_name)
        with open(save_path, 'w', encoding = 'utf-8-sig') as save_file:  
            df.to_csv(save_file)
    except FileNotFoundError:
        pass
    return df
    
if __name__ == '__main__':
    ...