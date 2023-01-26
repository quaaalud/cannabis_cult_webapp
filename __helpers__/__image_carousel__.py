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
    images_path = Path(Path(__file__).parent, '.data', 'carousel_images')
    return [
        str(pth) for pth in Path(images_path).iterdir() if Path(pth).is_file()
        ]


def _return_encoded_imgs_for_display(imgs_path: str):
    return [
        f'data:image/png;base64,{_return_url_bytes_str(img)}' for
        img in imgs_path
        ]

def _hide_loading_icon():
    hide_icon = """
    <style>
    div[data-testid="stToolbar"] {
    visibility: hidden;
    height: 0%;
    position: fixed;
    }
    div[data-testid="stDecoration"] {
    visibility: hidden;
    height: 0%;
    position: fixed;
    }
    div[data-testid="stStatusWidget"] {
    visibility: hidden;
    height: 0%;
    position: fixed;
    }
    </style>
    """
    st.markdown(hide_icon, unsafe_allow_html=True)


async def _return_image_carousel(set_height=300) -> components:
    _hide_loading_icon()
    main_block, display_block = st.empty(), st.empty()
    try:
        lib_dir = Path(
            'lib/python3.11/site-packages/Streamlit-Image-Carousel/frontend/public')
        image_carousel_component = components.declare_component(
            "image-carousel-component",
            path=f"{Path(__file__).parents[1]}/{lib_dir}"
            )
    except FileNotFoundError:
        image_carousel_component = components.declare_component(
            "image-carousel-component",
            path="/home/dale/dale_working_folder/mj_app/lib/python3.11/site-packages/Streamlit-Image-Carousel/frontend/public"
            )
    all_png_list = _return_img_carousel_files()
    png_urls = _return_encoded_imgs_for_display(all_png_list)
    with display_block:
        selected_image = image_carousel_component(
            imageUrls=png_urls,
            height=set_height
            )
    with main_block:
        selected_index = _return_index_of_list_item(png_urls, selected_image)
        if selected_image:
            await _display_selected_img(selected_image)
        else:
            while True:
                await _display_selected_img(png_urls[selected_index])
                await sleep_async(4)
                selected_index = (selected_index + 1) % len(png_urls)


def _get_indexed_list_dict(any_list: list) -> dict:
    return {index: item for index, item in enumerate(any_list)}


def _return_index_of_list_item(any_list: list, item) -> int:
    if item in any_list:
        temp_dict = {item: index for index, item in enumerate(any_list)}
        return temp_dict[item]
    else:
        return 0


async def wait_for_function(func, *args, **kwargs):
    async_task = asyncio.create_task(func(*args, **kwargs))
    async_result = await async_task
    return async_result


async def sleep_async(seconds):
    await asyncio.sleep(seconds)


async def _display_selected_img(img) -> st.image:
    return st.markdown(
        f"""
        <div
        style="display: flex; justify-content: center;
        max-height:250px;">
        <img style="text-align:center; width:auto";
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


if __name__ == '__main__':
    st.set_page_config(
        layout='wide',
        page_title='Cannabis Cult - Coming Soon',
        menu_items=None,
        initial_sidebar_state='collapsed',
    )
    asyncio.run(_return_image_carousel())
