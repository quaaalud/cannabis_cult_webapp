# -*- coding: utf-8 -*-

import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

def _get_landing_html():
    return """
        <div id="i6jtj" class="gpd-navbar">
          <div id="i6myg" class="gpd-container">
          </div>
        </div>
        <section id="ip0g" class="gpd-section">
          <div id="in36" class="gpd-container">
            <div id="ib8bg5" class="gdp-row gpd-grid">
              <div id="igar5v" class="cell gpd-clm">
                <h1 id="iyrzk" class="gpd-header">Subscribe for a chance to win the Rec-Day Party Pack! Featuring art by 
                  <span style="color:#e74c3c;">Ruby Pearl Co. </span>- Sponsored by 
                  <span style="color:#f39c12">Vivid Cannabis</span>
                  <br>
                </h1>
                <div id="ize3g" class="gpd-text">
                  <br>
                </div>
                <a id="iwur3" href="https://naturemedmo.com/ofallon/" target="_blank" class="gpd-link-box"></a>
                <a id="i6b1y" href="https://www.rubypearlco.com/" target="_blank" class="gpd-link-box"></a>
              </div>
              <div id="i65q8" class="cell gpd-clm">
                <a id="iblo5" href="https://www.vividcannabis.com/age-gate" target="_blank" class="gpd-link-box"></a>
                <form method="post" id="id3ai" data-redirect="" class="form">
                  <div id="isf5e" class="form-group">
                    <input type="text" placeholder="Email (Required)" name="firstname" id="i3ln7" class="input"/>
                    <input type="text" placeholder="Name" name="firstname" id="ixoo6" class="input"/>
                    <input type="text" placeholder="Zip Code" name="firstname" id="irlyz" class="input"/>
                    <input type="text" placeholder="Phone" name="firstname" id="i0n74" class="input"/>
                  </div>
                  <div id="Over the age of 21?" title="" class="form-group">
                    <input type="checkbox" name="checkbox-name" value="1" required id="ir7ah" class="checkbox"/>
                    <label for="" id="igd49" class="checkbox-label">By subscribing, you agree to the Cannabis Cult User Agreement and Privacy Statement, and that you are at least 21 years old.<br></label>
                  </div>
                  <div class="form-group">
                  </div>
                  <div class="form-group">
                  </div>
                  <div id="i7oaa" class="form-group">
                    <button type="submit" id="iru7x" class="button">Subscribe and Enter Giveaway</button>
                  </div>
                  <div data-form-state="success" id="islxo7" class="state-success">Thanks! We received your request
                  </div>
                  <div data-form-state="error" id="itmbfk" class="state-error">An error occurred on processing your request, try again!
                  </div>
                </form>
              </div>
            </div>
            <div id="i7u43" class="gpd-text">© 2023 The Social Outfit US. All rights reserved
              <br>
            </div>
          </div>
        </section>
        """


def local_css(file_path: str) -> str:
    with open(file_path) as f:
        css_str = f'<style>{f.read()}</style>'
    return css_str


def _return_copywrite_text():
    return """
    <section>
    <div>
    © 2023 The Cannabis Cult. All rights reserved
    </div>
    </section>
    """


def _apply_background():
    return """
    <style>
    .stApp {{
        background-image:url('https://cdn.grapedrop.com/u78fc0c652baa4df1a1b3109147139f84/daeaf6f75fd14e70980b4dfd6352b512_transparent_logo.png');
        background-repeat:no-repeat;
        background-position:top;
        background-size:cover;
        padding:5px 5px 5px 5px;
    }}
    </style>
    """


def return_giveaway_form():
    return """
    <div id="i65q8" class="cell gpd-clm">
       <form method="post" id="id3ai" data-redirect="" class="form">
         <div id="isf5e" class="form-group">
           <input type="text" placeholder="Email (Required)" name="firstname" id="i3ln7" class="input"/>
           <input type="text" placeholder="Name" name="firstname" id="ixoo6" class="input"/>
           <input type="text" placeholder="Zip Code" name="firstname" id="irlyz" class="input"/>
           <input type="text" placeholder="Phone" name="firstname" id="i0n74" class="input"/>
         </div>
         <div id="Over the age of 21?" title="" class="form-group">
           <input type="checkbox" name="checkbox-name" value="1" required id="ir7ah" class="checkbox"/>
           <label for="" id="igd49" class="checkbox-label">
           By subscribing, you agree to the Cannabis Cult User Agreement and Privacy Statement, and that you are at least 21 years old.
           <br>
           </label>
         </div>
         <div class="form-group">
         </div>
         <div class="form-group">
         </div>
         <div id="i7oaa" class="form-group">
           <button type="submit" id="iru7x" class="button">
           Subscribe and Enter Giveaway
           </button>
         </div>
         <div data-form-state="success" id="islxo7" class="state-success">
         Thanks! We received your request
         </div>
         <div data-form-state="error" id="itmbfk" class="state-error">
         An error occurred on processing your request, try again!
         </div>
       </form>
     </div>
     """


def _return_giveaway_text():
    return """
    <h1>
    Subscribe for a chance to win the Rec-Day Party Pack! Featuring art by
          <span style="color:#e74c3c;">Ruby Pearl Co. </span>- Sponsored by
          <span style="color:#f39c12">Vivid Cannabis</span>
      <br>
    </h1>
    """


if __name__ == '__main__':
    pass