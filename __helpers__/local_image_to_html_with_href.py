# -*- coding: utf-8 -*-

def _clickable_image_with_caption(web_path: str, img_path: str) -> str:
    from __get_image_to_display__ import _img_to_bytes
    _url = web_path.replace("https://", "")
    temp_url = _url.replace("www.instagram", "")
    clean_url = temp_url.replace(".com/", "")
    try:
        img_html = f"""
        <div style="text-align: center;">
        <a href='{web_path}'>
        <img src='data:image/png;base64,{_img_to_bytes(img_path)}'>
        <h4><u>{clean_url}</u></h4>
        </a>
        </div>
        """
    except:
        img_html = f"""
        <div style="text-align:center;">
        <a href='{web_path}'>
        <img src='data:image/jpg;base64,{_img_to_bytes(img_path)}'>
        <h4><u>{clean_url}</u></h4>
        </a>
        </div>
        """
    return img_html 


def _clickable_image_without_caption(web_path: str, img_path: str) -> str:
    from __get_image_to_display__ import _img_to_bytes
    try:
        img_html = f"""
        <div style="text-align: center;">
        <a href="{web_path}">
        <img src="data:image/png;base64,{_img_to_bytes(img_path)}">
        </a>
        </div>
        """
    except:
        img_html = f"""
        <div style="text-align:center;">
        <a href="{web_path}">
        <img src="data:image/jpg;base64,{_img_to_bytes(img_path)}">
        </a>
        </div>
        """
    return img_html 