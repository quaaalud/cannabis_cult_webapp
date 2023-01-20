# -*- coding: utf-8 -*-

import streamlit as st


def _return_centered_email() -> st.container:
    empty1, col, empty2 = st.columns([1, 5, 1])
    col.markdown(
        """
        <p>\n\n<br></p>
        <h3 style='text-align:center'>
        Send us an email today:
        <a href="mailto:dale.ludwinski@thesocialoutfitus.com"
        target="_blank"
        rel="noopener noreferrer">
        admin@cultcannabis.co
        </a>
        </h3>
        """,
        unsafe_allow_html=True,
        )