# src/utils.py
import logging
import streamlit as st
import os
import random


def initialize_project():
    """Creates the necessary folder structure automatically."""
    folders = [
        'data/raw', 
        'data/processed', 
        'data/assets', 
        'logs'
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    
    # Setup simple logging for the audit trail
    logging.basicConfig(
        filename='logs/project_log.txt',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Project directories initialized.")

def format_currency(value):
    return f"${value:,.2f}"


def add_sidebar_branding():
    """Restores the logo to the top-left position."""
    logo_path = "data/assets/CR_logo.png"
    if os.path.exists(logo_path):
        st.logo(logo_path, icon_image=logo_path)
    
    # The logo is placed here, navigation will follow automatically

def add_sidebar_footer():
    """Adds philosophical insights to the bottom of the sidebar."""
    insights = [
        "**Mass Balance:** Every $1 spike in HOEP must be recovered by a Δ of 1.0.",
        "**Gravity:** Energy is a physical commodity; it must return to the mean (OU Process).",
        "**Hedge Gap:** The delta between your Strike and Spot is your 'Unfunded Risk'.",
        "**The P.Eng Oath:** Protect the budget from catastrophic price spikes."
    ]
    st.sidebar.divider()
    st.sidebar.caption(f"🚀 **Antigravity Insight:**\n\n{random.choice(insights)}")
    # 2. Contact Info (Placed before navigation links in main.py)
    st.sidebar.markdown("**Contact & Support**")
    c1, c2 = st.sidebar.columns(2)
    with c1:
        st.sidebar.caption("[📧 Email](mailto:anjani@centauri-research.com)")
    with c2:
        st.sidebar.caption("[🌐 Website](https://centauri-research.com/)")