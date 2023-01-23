#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 18:36:21 2023

@author: dale
"""

import asyncio
import base64
import time
import streamlit as st
import streamlit.components.v1 as components
from st_clickable_images import clickable_images
from pathlib import Path


def _return_url_bytes_str(file_path: str):
    file_ = open(str(file_path), "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url


def _return_img_carousel_files() -> list:
    images_path = Path(Path(__file__).parent, '.data', 'png')
    return [
        str(pth) for pth in Path(images_path).iterdir() if Path(pth).is_file()
        ]


def _return_encoded_imgs_for_display(imgs_path: str):
    return [
        f'data:image/png;base64,{_return_url_bytes_str(img)}' for
        img in imgs_path
        ]


def _return_image_carousel(set_height=300) -> components:
    main_block, display_block = st.empty(), st.empty()
    try:
        webapp_dir = Path(__file__).parents[1]
        image_carousel_component = components.declare_component(
            "image-carousel-component",
            path=f"{webapp_dir}/lib/site-packages/Streamlit-Image-Carousel/frontend/public"
            )
    except st.errors.StreamlitAPIException:
        image_carousel_component = components.declare_component(
            "image-carousel-component",
            path="C:/Users/dludwinski/dale_working_folder/cannabis_cult_webapp/lib/site-packages/Streamlit-Image-Carousel/frontend/public"
            )
    all_png_list = _return_img_carousel_files()
    png_urls = _return_encoded_imgs_for_display(all_png_list)
    with display_block:
        selected_image = image_carousel_component(
            imageUrls=png_urls,
            height=set_height,
            )
    with main_block:
        if selected_image is None:
            _cycle_img_display(png_urls)
        else:
            _display_selected_img(selected_image)


def _cycle_img_display(img_url_list: list) -> None:
    for img in img_url_list:
        st.markdown(
            f"""
            <div
            style="display: flex; justify-content: center;
            max-height:250px; width: auto; height=auto;">
            <img style="text-align:center;";
            src="{img}">
            </div>
            """,
            unsafe_allow_html=True,
            )
        time.sleep(7)


async def _async_any_func(func, *args, **kwargs):
    _asynced = await func(*args, **kwargs)
    return _asynced


def _display_selected_img(img: str) -> st.image:
    return st.markdown(
        f"""
        <div
        style="display: flex; justify-content: center;
        max-height:250px; width:auto;">
        <img style="text-align:center;";
        src="{img}">
        </div>
        """,
        unsafe_allow_html=True,
        )


# Do not use this function unless you want a grid displaying images
def _return_image_selector(set_key=None) -> int:
    all_png_list =  _return_img_carousel_files()
    png_urls = _return_encoded_imgs_for_display(all_png_list)
    main_block = st.empty()
    with main_block:
        selected_image = clickable_images(
            png_urls,
            titles=[],
            div_style={
                "display": "flex",
                "justify-content": "center",
                "flex-wrap": "wrap"
                },
            img_style={
                "margin": "5px",
                "height": "200px",
                "text-align": "center",
                },
            key=set_key,
            )
    if selected_image >= 0:
        pass

def _test_main():
    _return_image_carousel()


if __name__ == '__main__':
    st.set_page_config(
        layout='wide',
        page_title='Cannabis Cult - Coming Soon',
        menu_items=None,
        initial_sidebar_state='collapsed',
    )
    _test_main()
