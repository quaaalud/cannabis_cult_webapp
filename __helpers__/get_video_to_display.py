#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 19:36:17 2023

@author: dale
"""

from pathlib import Path
import streamlit as st

MP4_PATH = Path(Path(__file__).parent, '.data', 'mp4')


def _get_all_videos(vid_path) -> dict:
    vid_types = ['.mp4', '.ogg', '.mov']
    return {Path(vid): Path(vid).suffix.strip('.') for vid in
            Path(vid_path).iterdir() if
            str(Path(vid).suffix).lower() in vid_types}


def _return_video_html(vid_bytes, vid_type) -> str:
    return f"""
    <div style="text-align:center;">
    <video controls;>
      <source src="{vid_bytes}" type="video/{vid_type}">
    </video>
    </div>
    """

@st.cache()
def _display_current_video(vid_path=MP4_PATH):
    vid_dict = _get_all_videos(vid_path)
    for vid_str, vid_type in vid_dict.items():
        with open(vid_str, 'rb') as open_vid:
            vid_bytes = open_vid.read() 
            return (vid_bytes, vid_type)
    

if __name__ == '__main__':
    print(_get_all_videos())
