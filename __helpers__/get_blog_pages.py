# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 18:46:19 2023

@author: dale
"""

import sys
from pathlib import Path
import streamlit as st


sys.path.append(str(Path(__file__).parent))


# @st.cache
def _get_list_blog_pages_dir():
    blog_dir = Path(Path(__file__).parent, '.data', 'blog_pages')
    return {
        _get_file_stem_from_path(file): _open_file_and_read_lines(file) for
        file in blog_dir.iterdir() if file.is_file()
    }


def _get_file_stem_from_path(file_path: str) -> str:
    return Path(file_path).stem


def _open_file_and_read_lines(file_path: str) -> str:
    with open(file_path, 'r') as file:
        contents = file.read()
    no_new_lines = ''.join(contents.splitlines())
    return no_new_lines


def display_blogs_as_tabs() -> None:
    """Create Streamlit tabs displaying html docs stored in blog_pages dir."""
    blog_dict = _get_list_blog_pages_dir()
    tabs_list = st.tabs([label for label in blog_dict.keys()])
    for t_index, tab in enumerate(tabs_list):
        for b_index, blog in enumerate(blog_dict.values()):
            if t_index == b_index:
                tab.markdown(blog, unsafe_allow_html=True)


if __name__ == '__main__':
    display_blogs_as_tabs()
